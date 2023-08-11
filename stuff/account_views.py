from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if request.POST.get('next') == 'None':
            redirect_to = '/'
        else:
            redirect_to = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user=user)
                return HttpResponseRedirect(redirect_to=redirect_to)
            else:
                return HttpResponse("Account has been disabled")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        next = request.GET.get('next')
        return render(request, 'stuff/login.html', {'next': next, })
