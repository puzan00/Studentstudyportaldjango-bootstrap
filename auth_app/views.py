# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        try:
            # Retrieve form data from POST request
            first_name = request.POST["firstname"]
            last_name = request.POST["lastname"]
            email = request.POST["email"]
            username = request.POST["username"]
            password = request.POST["password"]

            # Check for empty or spaces-only fields and minimum length
            if not (5 <= len(username.strip()) <= 30):
                messages.error(
                    request,
                    "Invalid input. Username should consist of at least 5 characters.",
                )
                return redirect("register")

            # Check minimum length for password
            min_password_length = 8
            if len(password) < min_password_length:
                messages.error(
                    request,
                    f"Password must be at least {min_password_length} characters.",
                )
                return redirect("register")

            # Check if the username or email already exists
            if (
                User.objects.filter(username=username).exists()
                or User.objects.filter(email=email).exists()
            ):
                messages.error(request, "Username or email already exists.")
                return redirect("register")

            # Create a new user using Django's built-in User model
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )

            # Display success message and redirect to login page
            messages.success(request, "Account created successfully")
            return redirect("login")
        except KeyError:
            # Display error message and redirect to registration page
            messages.error(request, "Invalid form submission")
            return redirect("register")


def signin(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            # Redirect authenticated users to the home page
            return redirect("home")
        return render(request, "login.html")
    else:
        try:
            # Retrieve username and password from POST request
            entered_username = request.POST["username"]
            entered_password = request.POST["password"]

            # Check for empty or spaces-only fields
            if not entered_username.strip() or not entered_password.strip():
                messages.error(request, "Username and password are required.")
                return redirect("login")

            # Authenticate user using provided credentials
            user = authenticate(username=entered_username, password=entered_password)

            if user is not None:
                # Log in user and handle redirect if a next_url is provided
                login(request, user)
                next_url = request.GET.get("next")
                if next_url is not None:
                    return redirect(next_url)
                return redirect("home")
            else:
                # Display error message and redirect to login page
                messages.error(request, "Invalid username or password")
                return redirect("login")
        except KeyError:
            # Display error message and redirect to login page
            messages.error(request, "Invalid form submission")
            return redirect("login")


def signout(request):
    logout(request)
    return redirect("login")
