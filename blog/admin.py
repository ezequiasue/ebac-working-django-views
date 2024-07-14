from django.contrib import admin
from .models.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_at', 'updated_at')
    list_editable = ('status',)  # Permitir edição do campo 'status' diretamente na lista
    list_filter = ('status', 'created_at', 'updated_at', 'author')  # Adicionar filtros para status, datas e autor

admin.site.register(Post, PostAdmin)
