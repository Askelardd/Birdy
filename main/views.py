from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import logout


 # renderizacao das paginas
 
def index(request):
    return render(request, 'main\index.html')

def login_page(request):
    return render(request, 'main\login.html')

def register(request):
    if request.method == "GET":
        return render(request, 'main/register.html')

#sistema de login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login bem-sucedido!!!!!!!!')
                return redirect('index')  # Redirecione para a página desejada após o login
            else:
                messages.error(request, 'Credenciais inválidas. Verifique seu nome de usuário e senha.')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form})

#sistema de registro
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirecione para a página desejada após o registro
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})


#sistema de logout
def logout_view(request):
    logout(request)
    return redirect('index')