from django.urls import path
from . import views as user_views

urlpatterns = [
    path('registro/', user_views.registro, name='registro-user'),
    path('profile/', user_views.profile, name='profile-user'),
    

]