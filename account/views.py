from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from mainpage import views as mainpage_view
from django.contrib.auth.decorators import login_required
from .forms import UserForm, StudentForm
from django import forms
import pdb
from django.contrib.auth.forms import UserCreationForm

prev_url = None


def goto_login(request):
    global prev_url
    prev_url = request.META['HTTP_REFERER']  # HOW TO REDIRECT THE PAGE TO THE PREVIOUS ONE
    return render(request, 'account/logintemplate.html')


def make_login(request):
    global prev_url
    ppreve_url = prev_url
    prev_url = None
    user_id = request.POST.get('login_id_box', None)
    user_pw = request.POST.get('login_pw_box', None)
    user = authenticate(username=user_id, password=user_pw)
    if user is not None:
        login(request, user)
        return redirect(ppreve_url)
    else:
        context = {'is_incorrect': True}
        return render(request, 'account/logintemplate.html', context)


def make_signup(request):
    user_id = request.POST.get('username_box', None)
    pw = request.POST.get('pw_box', None)
    email = request.POST.get('email_box', None)
    sid = request.POST.get('sid_box', None)
    dept = request.POST.get('dept_box', None)
    major = request.POST.get('major_box', None)
    year = request.POST.get('year_box', None)

    dept_all = mainpage_view.get_all_dept()
    major_all = mainpage_view.get_all_major()

    if dept == "0" or major == "0":  # 부서 또는 전공이 입력되지 않은 경우
        return render(request, 'account/signuptemplate.html',
                      {'empty_slot': True, 'dept_list': dept_all, 'major_list': major_all})
    user = User.objects.filter(username=user_id)

    if len(user) == 1:  # 이미 아이디가 존재하는 경우
        return render(request, 'account/signuptemplate.html',
                      {'already_id': True, 'dept_list': dept_all, 'major_list': major_all})
    stu = Student.objects.filter(s_id=sid)
    if len(stu) == 1:  # 이미 학번(s_id)이 존재하는 경우
        return render(request, 'account/signuptemplate.html',
                      {'already_sid': True, 'dept_list': dept_all, 'major_list': major_all})

    m_obj = Major.objects.filter(m_name=major)
    d_obj = Department.objects.filter(d_name=dept)

    user = User.objects.create_user(username=user_id, password=pw, email=email)

    Student(user=user, s_id=sid, s_d=d_obj[0], s_m=m_obj[0], username=user_id, s_email=email, since_y=int(year)).save()
    login(request, user)
    return redirect('/mainpage/')


@login_required
def make_logout(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


def signup(request):
    global prev_url
    if request.method == "POST":
        # user_form = UserCreationForm(request.POST)
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = User.objects.create_user(username=user_form.cleaned_data['username'],
                                            password=user_form.cleaned_data['password'],
                                            email=user_form.cleaned_data['email'])
            student = student_form.save(commit=False)
            student.user = user
            year = request.POST.get('s_id', None)
            if year:
                year = int(year[0:4])
            student.since_y = year
            student.save()
            pprev_url = prev_url
            prev_url = None
            return redirect(pprev_url)
    else:
        user_form = UserForm()
        student_form = StudentForm()
    dept_list = mainpage_view.get_all_dept()
    major_list = mainpage_view.get_all_major()

    return render(request, 'account/signup.html',
                  {'user_form': user_form, 'student_form': student_form, 'dept_list': dept_list,
                   'major_list': major_list})
