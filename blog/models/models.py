from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):  
    
    STATUS = ((0, 'Draft'), (1, 'Publish'))
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    status = models.IntegerField(choices=STATUS, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
