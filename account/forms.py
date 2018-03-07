from django import forms
from .models import Student, Department, Major
from django.contrib.auth.models import User


# class UserForm(forms.ModelForm):
#     class Meta:
#         fields = '__all__'
#         model = User

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    email = forms.CharField(max_length=50)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['s_id', 's_d', 's_m']
