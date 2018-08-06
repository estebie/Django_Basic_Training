from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from .utils import code_generator

User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    def toggle_follow(self, request_user, username_to_toggle):
        username_to_toggle.strip()
        profile = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = request_user
        is_following = False
        if user in profile.followers.all():
            profile.followers.remove(user)
        else:
            profile.followers.add(user)
            is_following = True
        return profile, is_following

class Profile(models.Model):
    user           = models.OneToOneField(User)
    followers      = models.ManyToManyField(User, related_name="is_following", blank=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated      = models.BooleanField(default=False)
    timestamp      = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            path = reverse('activate', kwargs={'code': self.activation_key})
            subject = 'Activate your account!'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Activate your account here: {path}'
            recipient_list = [self.user.email]
            html_message = f'<h1>Activate your account here: {path}</h1>'
            print(message)
            send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
        

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        default_user_profile.followers.add(instance)
        profile.followers.add(default_user_profile.user)

post_save.connect(post_save_user_receiver, sender=User)
