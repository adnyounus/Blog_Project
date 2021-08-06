from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def profile(request):
	return render(request, 'blog/profile.html')

def delete_post(request):
	p = Post.objects.get(pk=request.POST.get('id', ''))
	p.delete()
	messages.info(request, 'Post deleted successfully')
	return redirect('blog-home')

def delete_post_form(request, id):
	p = Post.objects.get(pk=id)
	context = {
		'id' : id,
		'title' : p.title
	}
	return render(request, 'blog/delete_post.html', context)

def edit_post(request):
	id_ = request.POST.get('id', '')
	p = Post.objects.get(pk=id_)

	p.title = request.POST.get('title', '')
	p.content = request.POST.get('content', '')

	p.save()

	messages.info(request, 'Post updated successfully')
	return redirect('blog-home')


def edit_post_form(request, id):
	p = Post.objects.get(pk=id)
	context = {
		'id' : id,
		'title' : p.title,
		'content' : p.content
	}
	return render(request, 'blog/edit_post.html', context)


def create_post(request):
	id_ = request.user.id
	title_ = request.POST.get('title', '')
	content_ = request.POST.get('content', '')
	p = Post(title=title_, content=content_, author_id=id_)
	p.save()
	messages.info(request, 'Post created successfully')
	return redirect('blog-home')


def create_post_form(request):
	return render(request, 'blog/create_post.html')

def user_logout(request):
	logout(request)
	return redirect('blog-home')

def user_login(request):
	if (request.user.is_authenticated):
		return redirect('blog-home')
	else:		
		return render(request, 'blog/login.html')

def user_login_verify(request):
	user_ = request.POST.get('username', '')
	pass_ = request.POST.get('password', '')

	user = authenticate(username=user_, password=pass_)

	if user is not None:
		login(request, user)
		return redirect('blog-home')
	else:
		messages.error(request, 'Incorrect Username/Password')
		return redirect('blog-login')


def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)
	# return HttpResponse('<h1>Hello, welcome to our blog</h1>')

@login_required
def about(request):
	return render(request, 'blog/about.html', {'title' : 'About Page'})
	# return HttpResponse('<h1>About Page</h1><h2>A CSE-465 Project</h2>')

# Create your views here.
