from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View

from .forms import ItemForm
from .models import Item

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('/login')
            # return render(request, "registration/login.html", {})
        
        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True)
        print(qs)
        return render(request, "home.html", {'object_list': qs})

class ItemListView(ListView, LoginRequiredMixin):
    login_url = '/login/'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView, LoginRequiredMixin):
    login_url = '/login/'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView, LoginRequiredMixin):
    form_class = ItemForm
    login_url = '/login/'
    template_name = 'form.html'
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['title'] = "Add Item"
        context['return_url'] = reverse('menus:list')
        return context     

class ItemUpdateView(UpdateView, LoginRequiredMixin):
    form_class = ItemForm
    login_url = '/login/'
    template_name = 'menus/detail-update.html'
    
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemUpdateView, self).form_valid(form)
        
    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Make Changes:"
        context['return_url'] = reverse('menus:list')
        return context           
# Create your views here.
