from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about, name='blog-about'),
    url(r'^apply/(?P<post>\d+)/$', views.apply_to_job, name='apply_to_job'),
    url(r'^delete/(?P<application>\d+)/$', views.delete_application, name='delete_application'),
    url(r'^accept/(?P<application>\d+)/$', views.accecpt_application, name='accecpt_application'),
    url(r'^decline/(?P<application>\d+)/$', views.decline_application, name='decline_application'),

    path('', views.apply_to_job, name='apply_to_job'),


]
