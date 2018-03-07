from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# account/
urlpatterns = [
    path('login/', views.goto_login, name="goto_login"),
    path('make_login/', views.make_login, name="make_login"),
    path('make_login/', auth_views.login, name="make_login"),
    path('make_logout/', views.make_logout, name="make_logout"),
    path('signup/', views.signup, name="signup"),
]
