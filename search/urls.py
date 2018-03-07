from django.urls import path
from . import views
from rate import views as rate_views

urlpatterns = [
	path('lecture/', views.search_lecture, name="search_lecture"),
	path('professor/', views.search_professor, name="search_professor"),
	path('lecture/<int:pk>/', views.detail, name="detail"),
]