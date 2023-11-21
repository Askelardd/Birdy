from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from main.models import aluno
from .forms import RegistarAluno


def home(request): #ligações as paginas web
    return render (request, 'home.html')

def main(request):
    return render (request, 'main.html')

def licoes(request):
    return render (request, 'licoes.html')

def editar_aluno(request, aluno_id):
    
    
    aluno_obj = get_object_or_404(aluno, id_aluno=aluno_id)

    # Lógica de edição aqui, se necessário

    return render(request, 'editar_aluno.html', {'aluno_obj': aluno_obj})

def registro_view(request):
    if request.method == 'POST':
        form = RegistarAluno(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Substitua 'main' pelo nome da sua view principal após o registro.
            print(f"Novo usuário registrado: Nome={form.cleaned_data['nome']}, Email={form.cleaned_data['email']}, Senha={form.cleaned_data['senha']}")
    else:
        form = RegistarAluno()

    return render(request, 'home.html', {'form': form})

