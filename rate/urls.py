from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.goto_rate, name='goto_rate'),
    path('<int:pk>/rate-success/', views.rate, name='rate')
]
