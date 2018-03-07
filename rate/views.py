from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from search import views as search_views
from django.contrib.auth.decorators import login_required
import pdb


@login_required
def goto_rate(request, pk):
    # todo CHECK IF ALREADY DID IT
    lecture = Lecture.objects.get(pk=pk)
    lec_ratings = Rating.objects.filter(r_l_id=pk)
    username = request.user.username
    stu_by_fil = Student.objects.filter(username=username)
    # pdb.set_trace()
    for each in lec_ratings:
        if each.r_s.s_id == stu_by_fil[0].s_id:  # 평가한 적 있음
            # return search_views.detail(request, pk)
            return redirect('/search/lecture/'+str(pk)+'/')

    # 평가한 적 없음
    return render(request, 'rate/rate.html', {'lecture': lecture})


@login_required
def rate(request, pk):  # pk: lecture's primary key
    exam = float(request.POST.get('exam_box', None))
    quiz = float(request.POST.get('quiz_box', None))
    hw = float(request.POST.get('hw_box', None))
    att = float(request.POST.get('att_box', None))
    lec = float(request.POST.get('lec_box', None))
    comment = request.POST.get('comment_box', None)
    avg = (exam + quiz + hw + att + lec) / 5
    userid = request.user.username
    user = Student.objects.filter(username=userid)

    Rating(r_s=user[0], r_l=Lecture.objects.get(pk=pk), exam_rating=exam, quiz_rating=quiz,
           hw_rating=hw, att_rating=att, lec_rating=lec, comment=comment).save()

    return redirect('/search/lecture/' + str(pk) + '/', pk=pk)
