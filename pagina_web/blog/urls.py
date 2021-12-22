from django.urls import path, re_path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CommentCreateView, CategoriaPostListView, DatePostListView, TopPostListView 
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home-blog'),
    path('post/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/new_comment/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('listacategoria/<str:categoria>', CategoriaPostListView, name='lista-categoria'),
    #re_path(r'date=(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})', DatePostListView, name='date-list')
    path('date/', DatePostListView, name='date-list'),
    path('topposts/', TopPostListView, name='top-posts')
    

]