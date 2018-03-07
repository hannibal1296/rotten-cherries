from django.db import models
from mainpage.models import *
from account.models import *
from django.urls import reverse


class Professor(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_d = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name="소속대학")
    p_l_name = models.CharField(max_length=10, verbose_name="성")
    p_f_name = models.CharField(max_length=10, verbose_name="이름")
    p_gender = models.CharField(max_length=1, choices=(('M', '남'), ('F', '여')), verbose_name="성별")
    p_office_loc = models.IntegerField(verbose_name="건물번호")
    p_office_num = models.CharField(max_length=15, verbose_name="오피스번호",
                                    help_text="031-XXX-XXXX")
    p_email = models.EmailField(verbose_name="이메일")
    have_kname = models.CharField(
        max_length=1, choices=(('T', 'Yes'), ('F', 'No')),
        help_text="This is used exclusively for naming.", verbose_name="Is it Korean name ?")

    def __str__(self):
        name = ""
        if self.have_kname == "T":
            name = self.p_l_name + self.p_f_name
        else:
            name = self.p_f_name + " " + self.p_l_name
        return name + " - " + str(self.p_d)

    @staticmethod
    def get_absolute_url(self):
        return reverse('search_professor')

    class Meta:
        verbose_name = "교수"
        verbose_name_plural = "교수"


class Lecture(models.Model):
    l_id = models.AutoField(primary_key=True)
    l_name = models.CharField(max_length=20, verbose_name="강의명")
    l_p = models.ForeignKey(Professor, on_delete=models.PROTECT, verbose_name="담당교수")
    semester = models.CharField(max_length=10, verbose_name="학기", help_text="e.g. 2018 봄/가을")
    l_credit = models.IntegerField(verbose_name="학점")

    def __str__(self):
        return self.semester + " / " + self.l_name + " / " + str(self.l_p)

    class Meta:
        verbose_name = "강의"
        verbose_name_plural = "강의"
        unique_together = (('l_name', 'l_p'))
