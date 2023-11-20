from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from main.forms import alunoForm

def home(request): #ligações as paginas web
    return render (request, 'home.html')

def main(request):
    return render (request, 'main.html')

def licoes(request):
    return render (request, 'licoes.html')

#declaração do login
def adicionar_aluno(request):
    if request.method == 'POST':
        form = alunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('página_sucesso')  # redirecionar para uma página de sucesso
    else:
        form = alunoForm()

    return render(request, 'main/home.html', {'form': form})
        