from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def index(request):
    template_name = 'index1.html'
    context = {

    }
    return render(request, template_name, context)

def learn(request):
    template_name = 'learn.html'
    context = {

    }
    return render(request, template_name, context)

def read(request):
    template_name = 'read.html'
    context = {

    }
    return render(request, template_name, context)

def events(request):
    template_name = 'events.html'
    context = {

    }
    return render(request, template_name, context)

def gallery(request):
    template_name = 'gallery.html'
    context = {

    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {

    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'contact.html'
    context = {

    }
    return render(request, template_name, context)