from django.http import HttpResponse
from django.shortcuts import render, redirect
from BlogApp.models import Blog
from django.contrib import messages


# Create your views here.

def create_blog(request):
    if request.method == "POST":
        blog_model = Blog()
        blog_model.title = request.POST["title"]
        blog_model.content = request.POST["content"]
        blog_model.written_by = request.POST["written_by"]

        blog_model.save()
        messages.success(request, "Blog created Successfully!!")
        return redirect('../get_all_blog/')

    else:
        return render(request, 'create_blog.html')


def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.written_by = request.POST["written_by"]

        blog.save()
        messages.success(request, "Blog edited Successfully!!")
        return redirect('../get_all_blog/')

    else:
        return render(request, 'edit_blog.html', {'blog': blog})


def show_blogs(request):
    blog_list = Blog.objects.all()
    return render(request, 'show_all_blogs.html', {'blog_list': blog_list})


def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted.')
    return redirect('../get_all_blog/')

def show_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'show_blog.html', {'blog': blog})

