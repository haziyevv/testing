from django.shortcuts import render
from .models import List

def home(request):
    context = List.objects.all
    return render(request, 'home.html', {"all_items": context})

def about(request):
    my_name = "Farid Haziyev"
    return render(request, 'about.html', {"name": my_name})
