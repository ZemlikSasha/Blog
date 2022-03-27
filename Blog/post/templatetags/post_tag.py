from django import template
from post.models import Category, Posts

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('tags/last_posts.html')
def get_last_posts():
    posts = Posts.objects.filter(category__name='Latest')
    return {'last_posts': posts}
