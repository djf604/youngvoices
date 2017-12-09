from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect


from youngvoices.models import Profile
from youngvoices import quiz as quiz_

# Create your views here.
def register(request):
    print('Entering method')
    if request.method == 'POST':
        if request.POST.get('username'):
            print(request.POST)
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            Profile.objects.create(user=user)
            login(request, user)
        elif request.POST.get('loginusername'):
            user = authenticate(request, username=request.POST['loginusername'], password=request.POST['loginpassword'])
            if user is not None:
                login(request, user)
        return HttpResponseRedirect('/')
    elif request.method == 'GET':
        return render(request, 'youngvoices/signup2.html', {})

def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')

def quiz(request):
    if request.method == 'POST':
        # Put your code here
        quiz_.init(request)
        quiz_.quiz()
        return HttpResponseRedirect('/quiz')
    elif request.method == 'GET':
        return render(request, 'youngvoices/quiz.html', {})
