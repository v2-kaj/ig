from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django import forms
from .models import Deposit
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "savings/index.html")
    else:
        return HttpResponseRedirect(reverse("account"))

@login_required
def account_view(request):
    deposits = Deposit.objects.all().filter(deposited_by=request.user).order_by('-deposit_date')
    return render(request, "savings/account.html", {"deposits": deposits})

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("account"))
        else:
            return render(request, "savings/index.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "savings/index.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))