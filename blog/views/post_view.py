# views/post_view.py

from django.views import generic
from django.http import HttpResponse

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
