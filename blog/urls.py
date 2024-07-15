# blog/urls.py
from django.urls import path
from blog.views.post_view import PostView, PostDetail  # Ajuste conforme necessário

urlpatterns = [
    path('', PostView.as_view(), name='post_view'),  # URL para listar posts
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),  # URL para detalhes do post
]
