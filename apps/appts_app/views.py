from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Appt, ApptManager
from ..login_app.models import User, UserManager
from datetime import datetime, timedelta, time, date
from time import strftime
from django.contrib import messages
from django.db.models import Q

def index(request):
    print '%'*75
    print 'I am on the login reg page'
    print '%'*75
    return redirect(reverse ("login:index"))

def appts(request):
    print '%'*75
    print 'I am on the appts page'
    print '%'*75
    now = datetime.now()
    context = {
        'my_appt': Appt.objects.filter(user__id=request.session['user_id']),
        'appt': Appt.objects.all(),
        'date': datetime.now().date(),
        'my_future_appt': Appt.objects.filter(Q(my_date__gte=now) & Q(user__id=request.session['user_id'])).exclude(my_date__lte=now, my_date__gte=now).order_by('my_date'),
        'my_today_appt': Appt.objects.filter(Q(my_date__lte=now, my_date__gte=now) & Q(user__id=request.session['user_id'])).order_by('my_time')
    }

    return render(request, "appts_app/index.html", context)

def add(request):
    print '%'*75
    print 'I am on the add appts page'
    print '%'*75
    appt = Appt.ApptManager.add(request.POST)
    logged_in = User.objects.get(id=request.session['user_id'])

    if appt[0] == False:
        new_appt = Appt.objects.create(user = logged_in, my_task=request.POST['task'], my_date=request.POST['date'], my_time=request.POST['time'], my_status = 'Pending')
        new_appt.save()
        return redirect(reverse ('appts:appts'))
    else:
        errors = appt[1]
        for error in errors:
            messages.error(request, error)
        return redirect(reverse ('appts:appts'))

def edit(request, appt_id):
    print '%'*75
    print 'I am on the edit appts page'
    print '%'*75
    context = {
        'appt' : Appt.objects.get(id=appt_id)
    }
    return render(request, 'appts_app/edit.html', context)

def delete(request, appt_id):
    print '%'*75
    print 'I am on the delete appts page'
    print '%'*75
    appt = Appt.objects.get(id=appt_id)
    appt.delete()
    return redirect(reverse ('appts:appts'))

def update(request, appt_id):
    print '%'*75
    print 'I am on the process edit appts page'
    print '%'*75
    appt = Appt.ApptManager.add(request.POST)
    logged_in = User.objects.get(id=request.session['user_id'])

    if appt[0] == False:
        appt = Appt.objects.get(id=appt_id)
        appt.my_task = request.POST['task']
        appt.my_status = request.POST['status']
        appt.my_date = request.POST['date']
        appt.my_time = request.POST['time']
        appt.save()
        return redirect(reverse ('appts:appts'))
    else:
        errors = appt[1]
        for error in errors:
            messages.error(request, error)
        return redirect(reverse ('appts:edit', kwargs={'appt_id':appt_id}))

def logout(request):
    request.session.clear()
    return redirect(reverse ("login:index"))
