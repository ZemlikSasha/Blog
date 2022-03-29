from django import template
from post.models import Category, Posts

register = template.Library()


@register.simple_tag()
def get_categories(): #ВЫЗЫВАЕМ ОБЪКТ ИЗ БАЗЫ ДАННЫХ
    return Category.objects.all()


@register.inclusion_tag('tags/last_posts.html')
def get_last_posts(): #ОБЪЯВЛЕНИЕ ФУНКЦИИ
    posts = Posts.objects.filter(category__name='Latest') #ФИЛЬТР ПОСЛЕДНИЕ
    return {'last_posts': posts} #СЛОВАРЬ ПОСЛЕНИХ ПОСТОВ
