from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from .models import Post, Comment
from user.models import Profile



# Create your views here.
"""
def PostListView(request):
    context = {
        'posts': Post.objects.all()
    }
    try:
        if request.GET['date'] is not None:
            print('estoy en el index')
            return redirect('data'+request.GET['date'])
    except :
        return render(request, 'blog/home.html', context)
    #return render(request, 'blog/home.html', context)  """

#Vista que maneja la Home

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4
    

#Vista que muestra los post por Usuario

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(autor=user).order_by('-date_posted')

"""class CategoriaPostListView(ListView):
    model = Post
    template_name = 'blog/categoria_post.html'
    context_object_name = 'categoria'
    extra_context = {
        'categoria': categoria,
    }
    paginate_by = 5

    def get_queryset(self):
        categoria = get_object_or_404(Post, categoria = self.kwargs.get('categoria'))
        return Post.objects.filter(categoria=categoria).order_by('-date_posted')"""
#Vista que muestra los post por Categoria

def CategoriaPostListView(request, categoria):
	posts = Post.objects.filter(categoria=categoria)
	context = {
        'categoria': categoria,
		'posts': posts}
	return render(request,'blog/categoria_post.html', context)

#Vista que muestra los post por Fecha

def DatePostListView(request):
    date = request.GET.get('date','')
    posts = Post.objects.filter(date_posted__contains = date)
    
    context = {
        'date': date,
        'posts': posts}
    return render(request,'blog/date_post.html', context)

#Vista que muestra los post con mas comentarios, solo los primeros 20

def TopPostListView(request):
    posts = Post.objects.raw('SELECT *, (SELECT COUNT(*) FROM blog_comment as bc WHERE bp.id = bc.post_id) as cantidad_comentarios FROM blog_post as bp ORDER BY cantidad_comentarios DESC LIMIT 20')
    context = {
        'posts': posts}
    return render(request,'blog/top_posts.html', context)


#Vista que muestra los post

class PostDetailView(DetailView):
    model = Post

#Vista que maneja la creacion de post

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('blog.add_post')
    model = Post
    fields = ['categoria','titulo', 'contenido']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
#Vista que maneja la creacion de comentarios

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    
    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
        

#Vista que maneja el update de post
    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        else:
            return False

#Vista que maneja el borrado de post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        else:
            return False
    




    