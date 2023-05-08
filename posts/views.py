from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Post, Comment
from .forms import PostForm
from django.views import generic



def home(request):
    return HttpResponse('<h1>Welcome to my Weblog</h1>')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/list.html', context=context)

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/list.html'
    context_object_name = 'posts'


def post_detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    comment = Comment.objects.filter(post=post)
    context = {'post': post, 'comment': comment}
    return render(request, 'posts/detail.html', context=context)
class PostDetial(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetial, self).get_context_data()
        context['comment'] = Comment.objects.filter(post=kwargs['object'].pk)
        return context




def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm
    return render(request, 'posts/create.html', {'from': form})