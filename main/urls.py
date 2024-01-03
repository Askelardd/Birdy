from django import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('uc/', uc, name='uc'),  
    path('forum/', forum, name='forum'),
    path('cursos/', cursos, name='cursos'),
    path('perguntasMath/', perguntasMath, name='perguntasMath'),
    path('crudPerguntas/', crudPerguntas, name='crudPerguntas'),  
    path('crudQuestoes/', crudQuestoes, name='crudQuestoes'),  
    path('verificar_resposta/<int:pergunta_id>/', verificar_resposta, name='verificar_resposta'),
    path('perguntas-math/<str:categoria>/', perguntasMath, name='perguntasMath'),

    
    path('crud_Perguntas/', criar_form_perg, name='crud_perguntas'),
    path('editarPerguntas/', editarPerguntas, name='editarPerguntas'),
    path('crud_perguntas/editar/<int:pergunta_id>/', editar_pergunta, name='editar_pergunta'),
    path('crud_perguntas/deletar/<int:pergunta_id>/', deletar_pergunta, name='deletar_pergunta'),
    
    path('criar_questao/', criar_questao, name='criar_questao'),
    path('editar_questao/<int:questao_id>/', editar_questao, name='editar_questao'),
    path('deletar_questao/<int:questao_id>/', deletar_questao, name='deletar_questao'),
    path('editarQuestao/', editarQuestao, name='editarQuestao'),
 
    
    
    path('resposta/criar/<int:questao_id>/', criar_resposta, name='criar_resposta'),
    path('resposta/editar/<int:resposta_id>/', editar_resposta, name='editar_resposta'),
    path('resposta/deletar/<int:resposta_id>/', deletar_resposta, name='deletar_resposta'),
    path('crudRespostas/', crudRespostas, name='crudRespostas'),
    
    
    path('allCruds/', allCruds, name='allCruds'),
    
    

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
