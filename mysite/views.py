from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request,'acceuil.html' )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    context={'val':"Menu Acceuil"}
    return render(request,'magasin/home.html',context)
