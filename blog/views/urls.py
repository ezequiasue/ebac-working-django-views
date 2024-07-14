# core/urls.py
from django.urls import path
from .post_view import PostView

urlpatterns = [
    path('post/', PostView.as_view(), name='index'),  # Certifique-se de que o nome da URL é 'index'
]
