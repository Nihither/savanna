from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


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
    elif request.method == 'GET':
        redirect_to = request.GET.get('next')
        return render(request, 'stuff/login.html', {'next': redirect_to, })


def user_logout(request, next):
    if request.method == 'POST':
        redirect_to = request.POST.get('next')
        confirm = request.POST.get('submit')
        if confirm == 'Logout':
            logout(request)
            return HttpResponseRedirect(redirect_to='/accounts/login')
        else:
            return HttpResponseRedirect(redirect_to=redirect_to)
    elif request.method == 'GET':
        redirect_to = next
        return render(request, 'stuff/logout.html', {'next': redirect_to, })