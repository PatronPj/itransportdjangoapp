from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


from .models import Post
from .models import Application
from .models import User
from django.utils import timezone

def home(request, page=0):
    if page == -1:
        page = 1
    articlesOnPage = 2
    offset = articlesOnPage * page
    posts = Post.objects.all()[offset:(offset+articlesOnPage)]
    pageAmount = len(Post.objects.all())/2
    if pageAmount.is_integer() == False:
        pageAmount += 1
    applications = Application.objects.all()
    return render(request, 'blog/home.html', {'posts': posts, 'applications':applications, 'page': (page+1), 'range': range(int(pageAmount)), 'pageAmount':pageAmount })

def apply_to_job(request, post):
    current_post = Post.objects.get(id=post)
    current_user = User.objects.get(id=request.user.id)
    Application.apply_to_job(current_user, current_post)
    post = Post.objects.all()
    post = Post.objects.order_by('-date_posted')
    application = Application.objects.all()
    messages.success(request, f'Congratulations, you applied to a job!')
    return render(request, 'blog/home.html', {'posts': post, 'applications':application})

def delete_application(request, application):
    Application.delete_application(application)
    post = Post.objects.all()
    post = Post.objects.order_by('-date_posted')
    application = Application.objects.all()
    messages.info(request, f'You successfully deleted your declined application!')
    return render(request, 'blog/home.html', {'posts': post, 'applications':application})

def accecpt_application(request, application):
    Application.accecpt_application(application)
    post = Post.objects.all()
    post = Post.objects.order_by('-date_posted')
    application = Application.objects.all()
    messages.success(request, f'Congratulations, you accepted an application!')
    return render(request, 'blog/home.html', {'posts': post, 'applications':application})

def decline_application(request, application):
    Application.decline_application(application)
    post = Post.objects.all()
    post = Post.objects.order_by('-date_posted')
    application = Application.objects.all()
    messages.info(request, f'You declined an application!')
    return render(request, 'blog/home.html', {'posts': post, 'applications':application})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'price', 'weight', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'price', 'weight', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url= '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
