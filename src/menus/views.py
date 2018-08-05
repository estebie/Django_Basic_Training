from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ItemForm
from .models import Item

class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
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
        return context     

class ItemUpdateView(UpdateView, LoginRequiredMixin):
    form_class = ItemForm
    login_url = '/login/'
    template_name = 'form.html'
    
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
        context['title'] = "Update Item"
        return context           
# Create your views here.
