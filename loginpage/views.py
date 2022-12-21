from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def loginpage(request):
    if request.method == 'GET':
        if request.user.is_authenticated: return redirect('/home/') 
        return render(request, 'loginpage.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/home/')
    else:
        context = {'error': 'Usuário ou senha incorretos'}
        return render(request, 'loginpage.html', context=context)


