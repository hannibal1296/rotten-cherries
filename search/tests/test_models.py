from django.test import TestCase
from search.models import *
from django.contrib.auth.models import User


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # 생성을 해주어야 한다.
        dept = Department.objects.create(d_name="소프트웨어대학")
        major = Major.objects.create(m_d=dept, m_name="컴퓨터공학")

        prof = Professor.objects.create(p_d=dept, p_l_name="이", p_f_name="종욱", p_gender="M", p_office_loc=23412,
                                        p_office_num="032-123-1234", have_kname="T")

    def test_get_absolute_url(self):
        professor = Professor.objects.get(p_id=1)
        self.assertEquals(professor.get_absolute_url(), '/search/professor/')
