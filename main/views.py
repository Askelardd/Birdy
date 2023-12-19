import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from main.models import Pergunta
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import logout
from django.conf import settings
from django.utils.crypto import get_random_string

 # renderizacao das paginas
 
def index(request):
    return render(request, 'main\index.html')

def cursos(request):
    return render(request, 'main/cursos.html') 

def editarPerguntas(request):
    return render(request, 'main\editarPerguntas.html')

def crudPerguntas(request):
    perguntas = Pergunta.objects.all()
    return render(request, 'main/crudPerguntas.html',{'perguntas':perguntas}) 

def perguntasMath(request):
    print("Isto foi corrido")
    perguntas = Pergunta.objects.all()
    return render(request, 'main/perguntasMath.html', {'perguntas': perguntas})
    # return render(request, 'main/perguntasMath.html')

def uc(request):
    return render(request, 'main/uc.html')

def forum(request):
    return render(request, 'main/forum.html')

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
                messages.success(request, 'Login bem-sucedido!!!')
                return redirect('uc')  # Redirecione para a página desejada após o login
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


def verificar_resposta(request, pergunta_id):
    pergunta = Pergunta.objects.get(pk=pergunta_id)

    # Verifica se a resposta do usuário é igual à resposta correta
    resposta_usuario = request.GET.get('resposta', None)
    if resposta_usuario and resposta_usuario == pergunta.respostacerta:
        mensagem = "Resposta correta!"
        pontos = request.session.get('pontos', 0)
        pontos += 1
        request.session['pontos'] = pontos
        print(pontos)
        resposta = f"{mensagem} Pontos: {pontos}"
    else:
        resposta = "Resposta errada."
        
        request.session.clear()
    return HttpResponse(resposta) 

# def criar_form_perg(request):
        
#     if request.method == 'POST':
#         pergunta_texto = request.POST.get('Pergunta')
#         imagem = request.FILES.get('Imagem')
#         resposta1 = request.POST.get('Resposta1')
#         resposta2 = request.POST.get('Resposta2')
#         resposta3 = request.POST.get('Resposta3')
#         resposta4 = request.POST.get('Resposta4')
#         respostacerta = request.POST.get('RespostaCorreta')
#         solucao = request.FILES.get('Solucao')
#         nova_pergunta = Pergunta.objects.create(
#             pergunta_texto=pergunta_texto,
#             imagem = imagem,
#             resposta1=resposta1,
#             resposta2=resposta2,
#             resposta3=resposta3,
#             resposta4=resposta4,
#             respostacerta=respostacerta,
#             solucao = solucao
#         )
#         nova_pergunta.save()
#         return HttpResponseRedirect(reverse('crudPerguntas'))

def criar_form_perg(request):
    if request.method == 'POST':
        pergunta_texto = request.POST.get('Pergunta')
        imagem = request.FILES.get('Imagem')
        resposta1 = request.POST.get('Resposta1')
        resposta2 = request.POST.get('Resposta2')
        resposta3 = request.POST.get('Resposta3')
        resposta4 = request.POST.get('Resposta4')
        respostacerta = request.POST.get('RespostaCorreta')
        solucao = request.FILES.get('Solucao')

        # Gere um nome de arquivo único para as imagens
        imagem_nome = f"imagem_{get_random_string(6)}.png"
        solucao_nome = f"solucao_{get_random_string(6)}.png"

        # Caminhos completos dos arquivos
        imagem_path = os.path.join(settings.MEDIA_ROOT, 'assets', imagem_nome)
        solucao_path = os.path.join(settings.MEDIA_ROOT, 'assets', solucao_nome)

        # Salve os arquivos no sistema de arquivos
        with open(imagem_path, 'wb') as imagem_file:
            for chunk in imagem.chunks():
                imagem_file.write(chunk)

        with open(solucao_path, 'wb') as solucao_file:
            for chunk in solucao.chunks():
                solucao_file.write(chunk)

        # Crie os URLs completos para os arquivos
        imagem_url = os.path.join('assets', imagem_nome)
        solucao_url = os.path.join('assets', solucao_nome)

        nova_pergunta = Pergunta.objects.create(
            pergunta_texto=pergunta_texto,
            imagem=imagem_url,
            resposta1=resposta1,
            resposta2=resposta2,
            resposta3=resposta3,
            resposta4=resposta4,
            respostacerta=respostacerta,
            solucao=solucao_url
        )
        nova_pergunta.save()
        return HttpResponseRedirect(reverse('crudPerguntas'))

    return render(request, 'main/crudPerguntas.html')

def editar_pergunta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    if request.method == 'POST':
        pergunta.pergunta_texto = request.POST.get('pergunta_texto')
        pergunta.imagem = request.FILES.get('imagem')
        pergunta.resposta1 = request.POST.get('resposta1')
        pergunta.resposta2 = request.POST.get('resposta2')
        pergunta.resposta3 = request.POST.get('resposta3')
        pergunta.resposta4 = request.POST.get('resposta4')
        pergunta.respostacerta = request.POST.get('respostacerta')
        pergunta.solucao = request.FILES.get('solucao')
        pergunta.save()
        mensagem = "Pergunta editada com sucesso."
        return HttpResponse(mensagem)

    return render(request, 'main/editarPerguntas.html', {'pergunta': pergunta})

def deletar_pergunta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    pergunta.delete()
    return redirect('crudPerguntas')