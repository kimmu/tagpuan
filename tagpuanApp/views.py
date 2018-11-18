from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Lost, Found, Post, Tag, Attach
from django.contrib.auth import login, logout



# Create your views here.
@login_required(login_url='/')
def home(request):
    username = request.session.get('username')
    args = {'username': username}
    return render(request, 'tagpuanApp/home.html', args)


def register(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            # log in
            user = form.save()
            login(request, user)
            #username = request.POST['username']
            # add to session variables: username
            request.session['username'] = request.user.username
            request.session['user'] = request.user.pk
            return redirect('userprofile')
    else:
        form = RegistrationForm()
    return render(request, 'tagpuanApp/register.html', {'form': form})


@login_required(login_url='/')
def create_userprofile(request):
    if (request.method == 'POST'):
        form = CreateUserProfile(request.POST)
        if (form.is_valid()):
            userprofile = form.save(commit=False)
            username = request.session.get('username')
            userprofile.user = request.user
            userprofile.save()
            return redirect('home')
    else:
        form = CreateUserProfile()
    return render(request, 'tagpuanApp/userprofile.html', {'form': form})


def login_view(request):
    if (request.method == 'POST'):
        form = LoginForm(data=request.POST)
        if (form.is_valid()):
            # log in user
            user = form.get_user()
            login(request, user)
            # add to session variables: username
            request.session['username'] = user.username
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'tagpuanApp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def add_post(request):
    if (request.method == 'POST'):
        form = AddPostForm(request.POST or None, request.FILES or None)
        user = User.objects.get(username=request.user.username)

        if (form.is_valid()):
            instance = form.save(commit=False)
            instance.user = user
            instance.save()

            # Find post instance equivalent to the post_id of
            # newly saved object. Then create a lost instance
            # with the post_id as foreignkey
            post_instance = Post.objects.get(post_id=instance.post_id)
            lost_instance = Found(post_id=post_instance)
            if (request.POST.get('post_type') == 'Lost'):
                lost_instance = Lost(post_id=post_instance)
            lost_instance.save()

            # Handling tags
            tags_string = request.POST.get('tags')
            tags_list = tags_string.split(",")
            for i in tags_list:
                i.lstrip()
                i.strip()
                print(i)
                tag_results = Tag.objects.filter(tag=i).count()
                if (tag_results==0):
                    new_tag = Tag(tag=i)
                    new_tag.save()

                tag_instance = Tag.objects.get(tag=i)
                attach_instance = Attach(tag_id=tag_instance, post_id=post_instance)
                attach_instance.save()




            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'tagpuanApp/addpost.html', {'form': form})
