from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('uc/', uc , name='uc'),
    path('uc/', uc , name='uc'),
    path('forum/', forum , name='forum'),
    path('cursos/', cursos , name='cursos'),
    path('perguntasMath/', perguntasMath , name='perguntasMath'),
    path('verificar_resposta/<int:pergunta_id>/', verificar_resposta, name='verificar_resposta'),
    path('crudPerguntas/', crudPerguntas, name='crudPerguntas'),
    path('editarPerguntas/', editarPerguntas, name='editarPerguntas'),
    path('crud_Perguntas/', criar_form_perg, name='crud_perguntas'),
    path('crud_perguntas/editar/<int:pergunta_id>/', editar_pergunta, name='editar_pergunta'),
    path('crud_perguntas/deletar/<int:pergunta_id>/', deletar_pergunta, name='deletar_pergunta'),
    path('perguntas-math/<str:categoria>/', perguntasMath, name='perguntasMath'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)