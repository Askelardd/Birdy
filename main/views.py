from functools import wraps
import os
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from main.models import *
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import logout
from django.conf import settings
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import user_passes_test


 # renderizacao das paginas
 
def index(request):
    return render(request, 'main\index.html')

def cursos(request):
    return render(request, 'main/cursos.html') 


def editarPerguntas(request):
    return render(request, 'main\editarPerguntas.html')


def editarQuestao(request):
    return render(request, 'main\editarQuestao.html')


def crudQuestoes(request):
    questoes = Questao.objects.all()
    topicos = Topico.objects.all()
    return render(request, 'main/crudQuestoes.html', {'questoes': questoes, 'topicos': topicos})

def is_professor(user):
    return user.is_authenticated and user.perfil.tipo_usuario == 'professor' or 'admin'

@user_passes_test(is_professor, login_url='index')#criar pagina de acesso negado

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

    # Defina uma resposta padrão
    resposta = ""

    # Verifica se a resposta do usuário é igual à resposta correta
    resposta_usuario = request.GET.get('resposta', None)
    if resposta_usuario and resposta_usuario == pergunta.respostacerta:
        mensagem = "Resposta correta!"

        usuario_existente = request.user

        # Tenta obter o perfil do usuário, cria um novo se não existir
        try:
            perfil_usuario = Perfil.objects.get(user=usuario_existente)
        except Perfil.DoesNotExist:
            perfil_usuario = Perfil(user=usuario_existente, tipo_usuario='aluno', pontos=0)
            perfil_usuario.save()

        if perfil_usuario.tipo_usuario == 'aluno':
            pontos_atuais = perfil_usuario.pontos
            perfil_usuario.pontos += 10  # Adiciona 10 pontos, por exemplo
            perfil_usuario.save()
            resposta = f"{mensagem} Pontos: {pontos_atuais}"
            
    else:
        resposta = "Resposta errada."
        
        # Limpar a sessão se a resposta estiver errada
        request.session.clear()

    # Retorna a resposta
    return HttpResponse(resposta)
    

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
        categoria = request.POST.get('Categoria')

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
            solucao=solucao_url,
            categoria = categoria
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


def perguntasMath(request, categoria=None):
    if categoria:
        perguntas = Pergunta.objects.filter(categoria=categoria)
    else:
        perguntas = Pergunta.objects.all()

    return render(request, 'main/perguntasMath.html', {'perguntas': perguntas, 'categoria_selecionada': categoria})


def forum(request):
    topicos = Topico.objects.all()
    questoes_por_topico = {}

    for topico in topicos:
        # Filtrar as questões relacionadas a cada tópico
        todas_questoes = Questao.objects.filter(topico=topico)
        questoes_e_respostas = []

        for questao in todas_questoes:
            # Para cada questão, obter suas respostas
            respostas = Resposta.objects.filter(questao=questao)
            questoes_e_respostas.append({'questao': questao, 'respostas': respostas})

        questoes_por_topico[topico] = questoes_e_respostas

    return render(request, 'main/forum.html', {'topicos': topicos, 'questoes_por_topico': questoes_por_topico})



def criar_questao(request):
    if request.method == 'POST':
        topico_id = request.POST.get('topico')
        pergunta = request.POST.get('pergunta')

        if topico_id and pergunta:
            topico = Topico.objects.get(id=topico_id)
            nova_questao = Questao.objects.create(topico=topico, autor=request.user, pergunta=pergunta)
            return redirect('forum')

    topicos = Topico.objects.all()
    return render(request, 'sua_template.html', {'topicos': topicos})

def editar_questao(request, questao_id):
    questao = get_object_or_404(Questao, id=questao_id)

    if request.method == 'POST':
        topico_id = request.POST.get('topico')
        pergunta = request.POST.get('pergunta')

        if topico_id and pergunta:
            topico = Topico.objects.get(id=topico_id)
            questao.topico = topico
            questao.pergunta = pergunta
            questao.save()
            return redirect('forum')

    topicos = Topico.objects.all()
    return render(request, 'main/editarQuestao.html', {'questao': questao, 'topicos': topicos})

def deletar_questao(request, questao_id):
    questao = get_object_or_404(Questao, id=questao_id)
    questao.delete()
    return redirect('forum')
