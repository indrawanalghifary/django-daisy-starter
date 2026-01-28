from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, template_name='dashboard.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")  # ganti sesuai tujuan setelah login
        else:
            messages.error(request, "Username atau password salah.")

    return render(request, "login.html")
