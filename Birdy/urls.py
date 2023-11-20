from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import adicionar_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('adicionar_aluno/', adicionar_aluno, name='adicionar_aluno'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)