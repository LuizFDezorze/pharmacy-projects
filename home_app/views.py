from django.shortcuts import render
from django.contrib.auth.models import User

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