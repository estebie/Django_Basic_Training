from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html", {"html_var" : True})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})
    