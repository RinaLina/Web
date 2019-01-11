from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=100, blank=True, verbose_name='Автор')
    publisher = models.CharField(max_length=100, blank=True, verbose_name='Издательство')
    year = models.IntegerField(blank=True, null=True, verbose_name='Год издания')
    pages = models.IntegerField(blank=True, null=True, verbose_name='Количество страниц')
    image = models.FileField(upload_to='images/', null=True, blank=True,
                             default='images/default_bookcover.jpg', verbose_name='Обложка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

class User(AbstractUser):
    favorite_author = models.CharField(max_length=40, blank=True, verbose_name='Любимый автор')
    about_me = models.TextField(max_length=1000, blank=True, verbose_name='О себе')
    books = models.ManyToManyField(Book, blank=True)
    image = models.FileField(upload_to='avatars/', null=True, blank=True,
                             default='avatars/default_avatar.png', verbose_name='Аватар')




