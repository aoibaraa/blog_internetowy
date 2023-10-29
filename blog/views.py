from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment, Profile
from .forms import UserRegistrationForm, UserLoginForm, PostForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def author_posts(request, author_id):
    author = get_object_or_404(User, id=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'blog/author_posts.html', {'author': author, 'posts': posts})


# Rejestracja użytkowników
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(request.POST.get('password'))
            user = form.save(commit=False)
            user.set_password(request.POST.get('password'))
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                profile.role = 'czytelnik'
                profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Panel logowania
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

# Proces wylogowania
def user_logout(request):
    logout(request)
    return redirect('home')

# Dodaj komentarz
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form': form})


# Tworzenie posta
@login_required
def create_post(request):
    user = request.user
    try:
        profile = user.profile
        if profile.role == 'redaktor':
            if request.method == 'POST':
                form = PostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.author = request.user
                    post.save()
                    return redirect('my_posts')
            else:
                form = PostForm()
            return render(request, 'blog/create_post.html', {'form': form})
        else:
            return HttpResponse("Brak uprawnień do tworzenia postów.")
    except Profile.DoesNotExist:
        return HttpResponse("Brak uprawnień do tworzenia postów.")


# Edycja posta
@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('my_posts')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/edit_post.html', {'form': form, 'post': post})
    else:
        return HttpResponse("Brak dostępu do edycji tego posta.")


# Usuwanie posta
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
        return redirect('my_posts')
    else:
        return HttpResponse("Brak dostępu do usunięcia tego posta.")


# Wyświetlanie listy swoich postów
@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})


# Dla admina - Panel admina
@user_passes_test(lambda u: u.is_staff)
def admin_panel(request):
    users = User.objects.all()
    return render(request, 'blog/admin_panel.html', {'users': users})
