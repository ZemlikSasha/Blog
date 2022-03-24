
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from .forms import ReviewForm
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
