from django.urls import path
from users.views import login, cadastro

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
]