from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('login/', views.login_view, name='login'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
