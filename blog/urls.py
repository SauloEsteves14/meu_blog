from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.listar_posts, name='post_list'),
    path('post/<int:post_id>/', views.detalhe_post, name='post_detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('comentario/<int:comentario_id>/editar/', views.editar_comentario, name='editar_comentario'),
    path('comentario/<int:comentario_id>/excluir/', views.excluir_comentario, name='excluir_comentario'),
    path('categoria/<int:categoria_id>/', views.posts_por_categoria, name='posts_por_categoria'),
]