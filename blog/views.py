from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import login
from .models import Post, Comment, Categoria
from .forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


def listar_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(titulo__icontains=query) | Q(conteudo__icontains=query)
        )

    posts = posts.order_by('-data_criacao')
    paginator = Paginator(posts, 5)  # 5 posts por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'categorias': categorias,
    })


def posts_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria).order_by('-data_criacao')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'categoria_nome': categoria.nome,
        'categorias': categorias,
    })


def detalhe_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comentarios = post.comentarios.order_by('-data_criacao')
    form = CommentForm()  # garante que sempre exista o formulário

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.post = post
                comentario.autor = request.user
                comentario.save()
                messages.success(request, "Comentário publicado com sucesso.")
                return redirect('post_detail', post_id=post.id)
            # Se não for válido, o form com erros será mostrado
        else:
            return redirect('login')  # se não autenticado, redireciona

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,  # garante sempre o form
    })


def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})


@login_required
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comment, pk=comentario_id)

    if request.user != comentario.autor:
        return HttpResponseForbidden("Você não tem permissão para editar este comentário.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comentario.post.id)
    else:
        form = CommentForm(instance=comentario)

    return render(request, 'blog/editar_comentario.html', {'form': form, 'comentario': comentario})


@login_required
def excluir_comentario(request, comentario_id):
    comentario = get_object_or_404(Comment, pk=comentario_id)

    if request.user != comentario.autor:
        return HttpResponseForbidden("Você não tem permissão para excluir este comentário.")

    if request.method == 'POST':
        post_id = comentario.post.id
        comentario.delete()
        messages.success(request, "Comentário excluído com sucesso.")
        return redirect('post_detail', post_id=post_id)

    return render(request, 'blog/excluir_comentario.html', {'comentario': comentario})


def posts_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria).order_by('-data_criacao')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'categoria_nome': categoria.nome,
    })