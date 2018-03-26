from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Major)
admin.site.unregister(Group)