from django.contrib import auth, messages
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.urls import reverse 


from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from products_app.models import Basket


# --------------------------------------------------------------------------------------------------------

def Login(request):
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]    
            
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main-page"))
    
    else:
        form = UserLoginForm()
    context = {
        "form": form
    }
    return render(request, "users/login.html", context)

# ----------------------------------------------------------------------------------------------------

def Register(request):
    if request.method == "POST":
        form = UserRegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cogratulations! you passed registration!")
            return HttpResponseRedirect(reverse("login-page"))
    else:
        form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context)

# --------------------------------------------------------------------------------------------------------

def Profile(request):
    if request.method == "POST":
        form = UserProfileForm(data = request.POST, instance = request.user, files = request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "your changes was saved")
            return HttpResponseRedirect(reverse("profile-page"))
    else:    
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    context = {
        "form": form,
        "baskets" : baskets,


    }
    return render(request, "users/profile.html", context)

# ----------------------------------------------------------------------------------------------------

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main-page"))


