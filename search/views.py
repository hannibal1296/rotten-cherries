from django.shortcuts import render, get_object_or_404
from mainpage.models import *
from account.models import *
from rate.models import *
from .models import *


def search_lecture(request):
    returns = []
    l_name = request.GET.get('search_lecture_box', None)
    l_obj = Lecture.objects.filter(l_name__contains=l_name).order_by('l_name')

    for each in l_obj:
        temp_p_obj = get_object_or_404(Professor, pk=each.l_p_id)
        # temp_p_obj = Professor.objects.get(pk=each.l_p_id)
        p_obj = Professor.objects.get(pk=temp_p_obj.p_id)
        name = None
        if p_obj.have_kname == "T":  # 한국이름
            name = p_obj.p_l_name + p_obj.p_f_name
        else:  # 영어이름
            name = p_obj.p_f_name + " " + p_obj.p_l_name
        returns.append([each, p_obj, "", name])

    return render(request, 'search/search_l_result.html', {'returns': returns})


def search_professor(request):
    profs = []
    p_name = request.GET.get('search_professor_box', None).lower()

    all_prof_names = []
    professors = Professor.objects.all()

    if len(professors) == 0:
        return render(request, 'search/search_p_result.html')
    for each in professors:
        if each.have_kname == 'T':
            all_prof_names.append([each.p_l_name.lower() + each.p_f_name.lower(), each])
        else:
            all_prof_names.append([each.p_f_name.lower() + " " + each.p_l_name.lower(), each])
    for i in range(len(all_prof_names)):
        if p_name in all_prof_names[i][0]:
            prof_obj = all_prof_names[i][1]
            # 한국어 이름
            if prof_obj.have_kname == "T":
                t_name = prof_obj.p_l_name + prof_obj.p_f_name
            # 영어 이름
            else:
                t_name = prof_obj.p_f_name + " " + prof_obj.p_l_name
            profs.append([prof_obj, t_name, Department.objects.get(pk=prof_obj.p_d_id).d_name])
    # 검색 결과 없음
    if len(profs) == 0:
        return render(request, 'search/search_p_result.html')
    else:
        return render(request, 'search/search_p_result.html', {'profs': profs})


def cal_rating(ratings):
    if not ratings:
        return None
    lec_sum = 0
    hw_sum = 0
    exam_sum = 0
    quiz_sum = 0
    att_sum = 0
    avg_sum = 0
    comments = []
    num_ratings = ratings.count()
    for each in ratings:
        lec_sum += each.lec_rating
        hw_sum += each.hw_rating
        quiz_sum += each.quiz_rating
        att_sum += each.att_rating
        exam_sum += each.exam_rating
        comments.append(each.comment)
    avg_sum = (lec_sum+hw_sum+quiz_sum+att_sum+exam_sum)/5
    return [round(exam_sum / num_ratings, 2), round(quiz_sum / num_ratings, 2), round(hw_sum / num_ratings, 2), \
            round(att_sum / num_ratings, 2), round(lec_sum / num_ratings, 2), round(avg_sum / num_ratings, 2)], comments


def detail(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    # lecture = Lecture.objects.get(pk=pk)
    p_id = lecture.l_p_id
    prof = get_object_or_404(Professor, pk=p_id)
    p_name = None
    if prof.have_kname == "T":  # 한국어 이름인 경우
        p_name = prof.p_l_name + prof.p_f_name
    else:  # 영어 이름인 경우
        p_name = prof.p_f_name + " " + prof.p_l_name
    ratings = Rating.objects.filter(r_l=pk)
    if len(ratings) == 0:  # 평가가 없을 때
        return render(request, 'search/lecture_detail.html', {'lecture': lecture, 'p_name': p_name})
    else:  # 기존의 평가가 존재할 때
        avg_rating, comments = cal_rating(ratings)
        return render(request, 'search/lecture_detail.html',
                      {'lecture': lecture, 'avg_rating': avg_rating,
                       'comments': comments, 'prof': prof, 'p_name': p_name})
