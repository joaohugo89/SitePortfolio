from django.shortcuts import render
from blogBack.models import Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, "blog/frontpage.html", {"posts":posts})

def about(request):
    return render(request, "blog/about.html")


