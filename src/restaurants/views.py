from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import RestaurantLocation

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    #template_name = 'restaurants/restaurants_list.html'
    
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__icontains = slug)|
                Q(category__iexact = slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        
        return queryset