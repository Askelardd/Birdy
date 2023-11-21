from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import editar_aluno,registro_view, login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('registro/', registro_view, name='registro'),
    path('editar_aluno/<int:aluno_id>/', editar_aluno, name='editar_aluno'),
    path('login/', login_view, name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)