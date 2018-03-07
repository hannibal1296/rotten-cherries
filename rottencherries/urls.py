from django.urls import path, include
from django.contrib import admin
from django.shortcuts import redirect


def root(request):
    return redirect('mainpage/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root, name='root'),
    path('mainpage/', include('mainpage.urls')),
    path('account/', include('account.urls')),
    path('search/', include('search.urls')),
    path('rate/', include('rate.urls')),
]
