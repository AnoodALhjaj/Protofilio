from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    Blogs=Blog.objects
    return render(request,"Blog.html",{"Blogs":Blogs})

def details(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)

    return render(request,"Detials.html",{"Blog":blog})