from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

class VerificarAutenticacaoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lista de páginas permitidas sem autenticação
        paginas_sem_autenticacao = ['/login/', '/register/', '/index/']

        if not request.user.is_authenticated and request.path_info not in paginas_sem_autenticacao:
            # Redireciona para a página de login se o usuário não estiver autenticado
            return redirect('index')

        response = self.get_response(request)
        return response
    
