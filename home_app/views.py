from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, "home_app/home.html")

# form de cadastro de users
def create(request):
    return render(request, "home_app/create.html")

# add data into the db
def store(request):
    data = {}
    if (request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senhas diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(
            request.POST['user'],
            request.POST['email'],
            request.POST['password']
        )
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'home_app/create.html', data)

# pag de login
def loginpage(request):
    return render(request, 'home_app/login_page.html')

# processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else: 
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'home_app/login_page.html', data)


# area privada
def dashboard(request):
    return render(request, 'home_app/dashboard.html')