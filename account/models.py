from django.db import models
from django.conf import settings
from django import forms
from django.shortcuts import reverse


def sid_validator(value):
    warning_sign = "학번이 올바르지 않습니다."
    if len(value) != 10:
        raise forms.ValidationError(warning_sign)
    # students = Student.objects.all()
    # for each in students:
    #     if each.s_id == value:
    #         raise forms.ValidationError(warning_sign)


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    s_id = models.CharField(unique=True, max_length=12, verbose_name="학번", validators=[sid_validator])
    s_d = models.ForeignKey('Department', models.PROTECT, verbose_name="소속대학")
    s_m = models.ForeignKey('Major', models.PROTECT, verbose_name="전공")
    since_y = models.IntegerField(verbose_name="입학연도", help_text="e.g. 2018")

    def __str__(self):
        return self.user.username + " - " + self.user.email

    class Meta:
        verbose_name = "학생"
        verbose_name_plural = "학생"


class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=20, verbose_name="학부", unique=True)

    def __str__(self):
        return self.d_name

    class Meta:
        verbose_name = "소속대학"
        verbose_name_plural = "소속대학"


class Major(models.Model):
    m_d = models.ForeignKey(Department, models.PROTECT, verbose_name="소속대학")
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=20, verbose_name="전공", unique=True)

    def __str__(self):
        return self.m_name

    class Meta:
        verbose_name = "전공"
        verbose_name_plural = "전공"
        unique_together = (('m_id', 'm_d'),)
