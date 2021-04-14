from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.Foreign.Key(
        to = 'Author'
        on delete = models.SET_NULL
        null=True, blank=True
        verbose_name='Автор',
        related_name='Автор'
    )

    readers = models.ManyToMany.Field(
        to = User,
        related_name = 'readed_articles',
        blank = True,
        verbose = name
    )


class Author(models.Models):
    user = MOdels.OneToOneField(
        to=User
        relatedname='author',
        verbos_name='пользователь',
        null = False,
        blank = False,
        on_delete=models.Cascade)

    nick = models.charfield(max_laength=55)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.nick