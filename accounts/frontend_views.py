from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("/")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()

def register_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Create user safely
        user = User.objects.create_user(username=username, password=password)

        # After registration go to login page
        return redirect("/login/")

    return render(request, "register.html")
