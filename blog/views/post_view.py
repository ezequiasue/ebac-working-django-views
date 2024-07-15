from django.views import generic
from blog.models import Post  # Certifique-se de que a importação está correta

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'  # Nome do template a ser usado
    context_object_name = 'posts'  # Nome do contexto a ser usado no template

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"  # Nome do template para detalhes do post


    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)  # Verifique se os posts estão sendo retornados
        return queryset
