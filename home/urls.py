from django.urls import path
from home import views

urlpatterns = [
    # Define a rota raiz que corresponde à função 'index' no arquivo 'views.py' dentro do aplicativo 'home'
    path('',views.index, name='index'),
    path('tags/',views.tags, name='tags'),
    path('pessoas/',views.pessoas, name='pessoas'),
    path('simula_leitura/',views.simula_leitura, name='simula_leitura'),
    path('leituras/',views.leituras, name='leituras'),
    path('vincular_tag_monitorado/',views.vincular_tag_monitorado, name='vincular_tag_monitorado'),
    path('criar_tag/',views.criar_tag, name='criar_tag'),
    path('criar_paciente/',views.criar_paciente, name='criar_paciente'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('local/<str:local_localizacao>/',views.local_detalhes, name='local_detalhes'),

    # user
    path('usuario/registrar/',views.registrar_usuario, name='registrar_usuario'),
    path('usuario/login/',views.login_view, name='login'),
    path('usuario/logout/',views.logout_view, name='logout'),

]



"""
Neste código:

urlpatterns é uma lista de objetos path que mapeiam URLs para funções de visualização (views).
path('', views.index, name='index') define a rota raiz do site, que corresponde à função de visualização index no arquivo views.py dentro do aplicativo home.
name='index' atribui um nome à rota, permitindo referenciar essa rota de forma única em todo o código Django. Isso é útil ao criar links em templates ou ao redirecionar para URLs internamente no código Python.
"""