from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

def home(request, name):
    user = User.objects.get(username=name)
    posts = Post.objects.filter(author=user)
    return render(request, 'blog/home.html', {'posts': posts})

def forum(request):
    posts = Post.objects.all()
    
    return render(request, 'blog/forum.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'The Post has been create successfully')
            return redirect('forum')     
        else:
            messages.error(request, 'Please correct the following errors')
            return render(request, 'blog/post_form.html', {'form': form})   
    
@login_required  
def edit_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)
    
    url = reverse('post-item', kwargs={'id': id})
    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated sucessfully')
            return redirect(url)
        else:
            messages.error(request, 'Pleases correct the following errors')
            return render(request, 'blog/post_form.html', {'form': form})

@login_required      
def delete_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)
    
    context = {'post': post}
    
    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)
    
    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'The post has been deleted successfully')
        return redirect('forum')
        


def post_item(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog/post.html", {'post': post})


def post_category(request, id):
    category = Category.objects.get(id=id)
    posts = Post.objects.filter(categories__title__in=[category])
    return render(request, 'blog/post_by_category.html', {'posts': posts})
