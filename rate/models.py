from django.db import models
from account.models import Student
from search.models import Lecture


# Create your models here.
class Rating(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_s = models.ForeignKey(Student, on_delete=models.CASCADE)
    r_l = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    exam_rating = models.FloatField(verbose_name="시험지수")
    quiz_rating = models.FloatField(verbose_name="퀴즈지수")
    hw_rating = models.FloatField(verbose_name="과제지수")
    att_rating = models.FloatField(verbose_name="출첵지수")
    lec_rating = models.FloatField(verbose_name="강의지수")
    comment = models.CharField(max_length=280, verbose_name="평가", help_text="280 Characters Limited")

    def __str__(self):
        return str(self.r_l)+ ": "+self.comment[0:10]

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰"
        unique_together = (('r_id', 'r_l', 'r_s'))
