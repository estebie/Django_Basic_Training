from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ItemForm
from .models import Item

class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemUpdateView(ListView):
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)       
# Create your views here.
