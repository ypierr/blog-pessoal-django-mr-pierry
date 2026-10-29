from django.shortcuts import render
from .models import Post
from .forms import ComentarioForm

def inicio(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, "blog/inicio.html", {"posts": posts})

def post_detalhe(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save
    else:
        form = ComentarioForm()

    return render(
        request,
        'blog/post_detalhe.html',
        {
            'post': post,
            'form': form,
        }
    )