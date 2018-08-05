from django.conf.urls import url

from .views import ProfileDetailview

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailview.as_view(), name ='profile')
]
