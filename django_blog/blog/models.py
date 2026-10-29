from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )
    nome = models.CharField(max_length=100)
    comentario = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.post.titulo}"