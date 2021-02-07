from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django import forms
from .models import Deposit
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "savings/index.html")
   