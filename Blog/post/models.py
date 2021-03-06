
from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):

    name = models.CharField('Category', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self): #вывод названий категорий(большие буквы)
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Posts(models.Model):

    title = models.CharField('Title', max_length=150)
    date = models.DateField('Date published', default=date.today)
    author = models.CharField('Author', max_length=100)
    category = models.ForeignKey(
        Category, verbose_name='Category', on_delete=models.SET_NULL, null=True
    )
    post = models.TextField('Post')
    url = models.SlugField(max_length=150, unique=True)
    image = models.ImageField('Image', upload_to='posts/')

    def __str__(self):
        return self.title #вывод названия статьи

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True) #отзывы с родителям

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'slug': self.url}) #возращение адресс поста

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Reviews(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    text = models.TextField('Text')
    post = models.ForeignKey(
        Posts, verbose_name='Review', on_delete=models.CASCADE
    ) #привязка отзыва к посту
    parent = models.ForeignKey(
        'self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True
    ) #выбор родителя

    def __str__(self):
        return f'{self.name} - {self.post}' #вывод имени и поста новостного

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class ReviewContact(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    text = models.TextField('Text')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Review Contact'
        verbose_name_plural = 'Reviews Contact'
