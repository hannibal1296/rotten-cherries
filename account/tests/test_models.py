from django.test import TestCase
from account.models import *
from django.contrib.auth.models import User


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # 생성을 해주어야 한다.
        dept = Department.objects.create(d_name="소프트웨어대학")
        major = Major.objects.create(m_d=dept, m_name="컴퓨터공학")

        uuser = User.objects.create(username="show7774", password="hannibal1296", email="show7774@gmail.com")
        Student.objects.create(user=uuser, s_id="2012313385", s_d=dept, s_m=major, since_y=2012)

    def test_first_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('s_id').verbose_name
        # 핵심 테스팅 부분
        self.assertEquals(field_label, '학번')

    def test_first_name_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('s_id').max_length
        self.assertEquals(max_length, 12)
