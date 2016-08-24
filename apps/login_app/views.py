from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserManager
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    print '%'*75
    print 'I am on the main login page'
    print '%'*75
    return render(request, 'login_app/index.html')

def register(request):
    print '%'*75
    print 'hit register'
    print '%'*75
    if request.method == 'POST':
        user = User.objects.register(request.POST)
    if user[0]:
        request.session['user_id'] = user[1].id
        request.session['first_name'] = user[1].first_name

        return redirect('appts:appts')

    for error in user[1]:
            messages.error(request, error)

    return redirect('/')

def login(request):
    print '%'*75
    print 'hit login'
    print '%'*75
    user = User.objects.login(request.POST)
    if user[0]:
        request.session['user_id'] = user[1].id
        request.session['first_name'] = user[1].first_name

        return redirect('appts:appts')

    for error in user[1]:
        messages.error(request, error)

    return redirect('/')
