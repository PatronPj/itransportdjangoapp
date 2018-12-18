from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from .models import Post
from .models import Application
from .models import User

def home(request, page=0, applied=0):
    if page == -1:
        page = 1
    articlesOnPage = 2
    offset = articlesOnPage * page
    subPosts = Post.objects.all()[offset:(offset+articlesOnPage)]
    subPosts = Post.objects.order_by('-date_posted')[offset:(offset+articlesOnPage)]
    pageAmount = len(Post.objects.all())/2
    if pageAmount.is_integer() == False:
        pageAmount += 1
    posts = Post.objects.all()
    applications = Application.objects.all()
    return render(request, 'blog/home.html', {'subPosts': subPosts, 'applications': applications, 'page': (page+1), 'range': range(int(pageAmount)), 'pageAmount': pageAmount, 'posts':posts, 'applied': applied})

def apply_to_job(request, post, page=0, applied=0):
    if page == -1:
        page = 1
    articlesOnPage = 2
    offset = articlesOnPage * page
    subPosts = Post.objects.all()[offset:(offset+articlesOnPage)]
    subPosts = Post.objects.order_by('-date_posted')[offset:(offset+articlesOnPage)]
    pageAmount = len(Post.objects.all())/2
    if pageAmount.is_integer() == False:
        pageAmount += 1

    current_post = Post.objects.get(id=post)
    current_user = User.objects.get(id=request.user.id)
    Application.apply_to_job(current_user, current_post)
    posts = Post.objects.all()
    posts = Post.objects.order_by('-date_posted')
    applications = Application.objects.all()
    messages.success(request, f'Congratulations, you applied to a job!')
    send_mail('Job Application', 'Congratulations, you applied to the job:'+current_post.title +'!', settings.EMAIL_HOST_USER, [current_user.email], fail_silently=False)
    send_mail('Job Application', 'The user ' + current_user.username + ' successfully applied to your offer: '+current_post.title +'.', settings.EMAIL_HOST_USER, [current_post.author.email], fail_silently=False)
    return render(request, 'blog/home.html', {'posts': posts, 'subPosts': subPosts, 'applications': applications, 'page': (page+1), 'range': range(int(pageAmount)), 'pageAmount': pageAmount, 'applied': applied})

def delete_application(request, application, page=0):
    if page == -1:
        page = 1
    articlesOnPage = 2
    offset = articlesOnPage * page
    subPosts = Post.objects.all()[offset:(offset+articlesOnPage)]
    subPosts = Post.objects.order_by('-date_posted')[offset:(offset+articlesOnPage)]
    pageAmount = len(Post.objects.all())/2
    if pageAmount.is_integer() == False:
        pageAmount += 1

    Application.delete_application(application)
    post = Post.objects.all()
    post = Post.objects.order_by('-date_posted')
    application = Application.objects.all()
    messages.info(request, f'You successfully deleted your declined application!')
    return render(request, 'blog/home.html', {'posts': post, 'applications': application, 'subPosts': subPosts, 'page': (page+1), 'range': range(int(pageAmount)), 'pageAmount': pageAmount})

def accecpt_application(request, application, page=0):
    if page == -1:
        page = 1
    articlesOnPage = 2
    offset = articlesOnPage * page
    subPosts = Post.objects.all()[offset:(offset+articlesOnPage)]
    subPosts = Post.objects.order_by('-date_posted')[offset:(offset+articlesOnPage)]
    pageAmount = len(Post.objects.all())/2
    if pageAmount.is_integer() == False:
        pageAmount += 1

    Application.accecpt_application(application)
    post = Post.objects.all()
    post = Post.objects.order_by('-date_posted')
    messages.success(request, f'Congratulations, you accepted an application!')
    return render(request, 'blog/home.html', {'posts': post, 'applications': application, 'subPosts': subPosts, 'page': (page+1), 'range': range(int(pageAmount)), 'pageAmount': pageAmount})


def decline_application(request, application, page=0):
    if page == -1:
        page = 1
    articlesOnPage = 2
    offset = articlesOnPage * page
    subPosts = Post.objects.all()[offset:(offset+articlesOnPage)]
    subPosts = Post.objects.order_by('-date_posted')[offset:(offset+articlesOnPage)]
    pageAmount = len(Post.objects.all())/2
    if pageAmount.is_integer() == False:
        pageAmount += 1

    Application.decline_application(application)
    post = Post.objects.all()
    post = Post.objects.order_by('-date_posted')
    application = Application.objects.all()
    messages.info(request, f'You declined an application!')
    return render(request, 'blog/home.html', {'posts': post, 'applications': application, 'subPosts': subPosts, 'page': (page+1), 'range': range(int(pageAmount)), 'pageAmount': pageAmount})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'price', 'weight', 'image', 'adress1', 'zip_code1', 'city1', 'adress2', 'zip_code2', 'city2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'price', 'weight', 'image', 'adress1', 'zip_code1', 'city1', 'adress2', 'zip_code2', 'city2']

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
