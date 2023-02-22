from django.shortcuts import get_object_or_404, redirect, render
from django import forms

from .models import Post


# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    post_list = Post.objects.order_by('-created_on')
    return render(request, 'home.html', {"post_list": post_list})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.content = request.POST.get('my_text_field')
        post.save()

    return render(request, 'post_detail.html', {"post": post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('home')

