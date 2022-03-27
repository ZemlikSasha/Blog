
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from .forms import ReviewForm, ReviewFormContact
from .models import Posts


class PostList(View):

    def get(self, request):
        posts_first = Posts.objects.all()[:4]
        posts_all = Posts.objects.all()
        return render(request, 'index.html', {'posts_first': posts_first, 'posts_all': posts_all})


def contact(request):
    return render(request, 'contact.html')


class PostDetail(DetailView):

    model = Posts
    slug_field = 'url'
    template_name = 'posts_detail.html'


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        post = Posts.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.post = post
            form.save()
        return redirect(post.get_absolute_url())


class ReviewContact(View):

    def post(self, request):
        form = ReviewFormContact(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
        return redirect('/')


class Category(View):

    def get(self, request, string):
        posts = Posts.objects.filter(category__name=string)
        first_post = posts[0]
        return render(request, 'category.html', {'first_post': first_post, 'posts_list': posts})
