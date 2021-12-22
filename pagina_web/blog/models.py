from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse
from user.models import Profile

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Categorias = [
        ('Fin de la pobreza', 'Fin de la pobreza'),
        ('Hambre Cero','Hambre Cero'),
        ('Salud y Bienestar','Salud y Bienestar'),
        ('Educacion de Calidad','Educacion de Calidad'),
        ('Igualdad de Genero','Igualdad de Genero'),
        ('Agua Limpia y Saneamiento','Agua Limpia y Saneamiento'),
        ('Energia Asequible y no Contaminante','Energia Asequible y no Contaminante'),
        ('Trabajo Decente y Crecimiento Economico','Trabajo Decente y Crecimiento Economico'),
        ('Agua, Industria, Innovacion e Infraestructura','Agua, Industria, Innovacion e Infraestructura'),
        ('Reduccion de las Desigualdades','Reduccion de las Desigualdades'),
        ('Ciudades y Comunidades Sostenibles','Ciudades y Comunidades Sostenibles'),
        ('Produccion y Consumos Responsables','Produccion y Consumos Responsables'),
        ('Accion por el Clima','Accion por el Clima'),
        ('Vida Submarina','Vida Submarina'),
        ('Vida de Ecosistemas Terrestres','Vida de Ecosistemas Terrestres'),
        ('Paz, Justicia e Instituciones Solidas','Paz, Justicia e Instituciones Solidas'),
        ('Alianzas para lograr los objetivos','Alianzas para lograr los objetivos'),

    ]
    categoria = models.TextField(max_length = 60, choices = Categorias, default = 'Fin de la pobreza')

    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})


