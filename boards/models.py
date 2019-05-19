from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Board(models.Model):
    name = models.CharField('Tablero', max_length=30, unique=True)
    description = models.CharField('Descripción', max_length=100)

    class Meta:
        verbose_name = 'Tablero'
        verbose_name_plural = 'Tableros'
        ordering = ['name']

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField('Tópico', max_length=255)
    last_updated = models.DateTimeField('Actualizado', auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics',
                              on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', null=True,
                                on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['subject']

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField('Mensaje', max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', null=True)
    created_by = models.ForeignKey(User, related_name='posts', null=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, null=True, related_name='+',
                                   on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['created_at']
