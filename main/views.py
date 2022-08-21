from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from . import models
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import re
import json

#pyTelegramBotAPI
# from multiprocessing import Process
# from . import telegram_api
# def pytelegrambotapi():
#     telegram_api.main()
# process1 = Process(target=pytelegrambotapi)
# process1.start()

login = ''
login_watch = ''
watch_status = 0
year = 0
month = ''


def year(request):
    global login, login_watch, watch_status
    try:
        watch_status = 0
        if request.POST.get('login', 0) != 0:
            login = request.POST['login']
            if login in [obj.login for obj in models.User.objects.all()]:
                models.User.objects.get_or_create(login=login, password=request.POST['password'],)
            else:
                return render(request, 'form.html', {'exists': 'account does not exists'})
        if request.POST.get('day', 0) != 0:
            user = models.User.objects.get(login=login)
            user.user_data_set.create(year=(request.POST['year']),
                                      day=(request.POST['day']),
                                      month=request.POST['month'],
                                      text=request.POST['note'])
        if request.GET.get('user', 0) != 0:
            login_watch = str(request.META['QUERY_STRING'][5:])
            watch_status = 1
        if request.POST.get('login_reg', 0) != 0:
            models.User.objects.get_or_create(login=request.POST['login_reg'], password=request.POST['password_reg'], name=request.POST['name'])
        if login in [obj.login for obj in models.User.objects.all()]:
            return render(request, 'year.html', {'login': login, 'my_data': {'2020': 1, '2021': 2}, 'name': models.User.objects.get(login=login).name})
        else:
            return form(request)
    except IntegrityError:
        return form(request)


def month(request):
    global year, login_watch, watch_status
    year = request.GET['year']
    list_months = []
    if watch_status:
        for obj in models.User_data.objects.all():
            if obj.login.login == login_watch and obj.year == int(year):
                if obj.month not in list_months:
                    list_months.append(obj.month)
        return render(request, 'month.html', {'my_data': list_months, 'year': year, 'name': models.User.objects.get(login=login_watch).name})
    list_months = []
    for obj in models.User_data.objects.all():
        if obj.login.login == login and obj.year == int(year):
            if obj.month not in list_months:
                list_months.append(obj.month)
    return render(request, 'month.html', {'my_data': list_months, 'year': year, 'name': models.User.objects.get(login=login).name})


def day(request):
    global year, month, login_watch, watch_status
    month = request.GET['month']
    list_days = []
    if watch_status:
        for obj in models.User_data.objects.all():
            if obj.login.login == login_watch and obj.year == int(year) and obj.month == month:
                if obj.day not in list_days:
                    list_days.append(obj.day)
        return render(request, 'day.html', {'my_data': list_days, 'year': year, 'month': month, 'name': models.User.objects.get(login=login_watch).name})
    for obj in models.User_data.objects.all():
        if obj.login.login == login and obj.year == int(year) and obj.month == month:
            if obj.day not in list_days:
                list_days.append(obj.day)
    return render(request, 'day.html', {'my_data': list_days, 'year': year, 'month': month, 'name': models.User.objects.get(login=login).name})


def note(request):
    global year, month, watch_status
    day = request.GET['day']
    if watch_status:
        for obj in models.User_data.objects.all():
            if obj.login.login == login_watch and obj.year == int(year) and obj.month == month and obj.day == int(day):
                return render(request, 'note.html',
                              {'my_data': [obj.text], 'year': year, 'month': month, 'day': request.GET['day'], 'name': models.User.objects.get(login=login_watch).name})
    for obj in models.User_data.objects.all():
        if obj.login.login == login and obj.year == int(year) and obj.month == month and obj.day == int(day):
            return render(request, 'note.html',
            {'my_data': [obj.text], 'year': year, 'month': month, 'day': request.GET['day'], 'name': models.User.objects.get(login=login).name})
    return render(request, 'note.html', {'year': year, 'month': month, 'day': request.GET['day']})


def form(request):
    try:
        pass
    except MultiValueDictKeyError:
        pass
    return render(request, 'form.html')


def users(request):
    users = []
    for user in models.User.objects.all():
        users.append(user.login)
    return render(request,'users_base.html', {'users': users, 'name': models.User.objects.get(login=login).name})


def new_note(request):
    return render(request, 'new.html', {'name': models.User.objects.get(login=login).name})


@csrf_exempt
def send_data(request):
    if request.method == 'GET':
        ans = []
        for obj in models.User_data.objects.all():
            if obj.login_id == login:
                resp = obj.text.replace(' ', '')
                km = re.findall(r'(\d*[,]?\d+)км', resp)
                m = re.findall(r'(\d*[,]?\d+)м', resp)
                total = 0
                for group_km in km:
                    if group_km[0] == ',':
                        group_km = group_km[1:]
                    group_km = group_km.replace(',', '.')
                    total += float(group_km)
                for group_m in m:
                    if group_m[0] == ',':
                        group_m = group_m[1:]
                    group_m = group_m.replace(',', '.')
                    total += float(group_m)/1000
                total *= 1.1
                ans.append(total)
        return HttpResponse(json.dumps({'response': ans}))



