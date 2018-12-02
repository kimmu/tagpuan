from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Lost, Found, Post, Tag, Attach, UserProfile
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
            return redirect('list_post')
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
            return redirect('list_post')
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




@login_required(login_url='/')
def profile_page(request):
    user = User.objects.get(username=request.user)
    user_instance = UserProfile.objects.get(user=user)
    username = request.session.get('username')
    args = {'username': username,
            'user_email': user.email,
            'phone_number': user_instance.phone_number,
            'birthdate': user_instance.date_of_birth,
            'first_name': user.first_name,
            'last_name': user.last_name,
            }
    return render(request, 'tagpuanApp/profilepage.html', args)
@login_required(login_url='/')
def Postprofile(request,pk):
    posts = get_object_or_404(Post, pk=pk)
    #user=posts.user
    #user_instance = UserProfile.objects.get(user=user)
    #args = {'username': username,
    #        'user_email': user.email,
    #        'phone_number': user_instance.phone_number,
    #        'birthdate': user_instance.date_of_birth,
    #        'first_name': user.first_name,
    #        'last_name': user.last_name,
    #        }
    return render(request, 'tagpuanApp/Postprofile.html', {'posts':posts})

@login_required(login_url='/')
def post_profile_page(request,pk):
    posts = get_object_or_404(Post, pk=pk)
    user=posts.user
    user_instance = UserProfile.objects.get(user=user)
    args = {'username': user.username,
            'user_email': user.email,
            'phone_number': user_instance.phone_number,
            'birthdate': user_instance.date_of_birth,
            'first_name': user.first_name,
            'last_name': user.last_name,
            }
    return render(request, 'tagpuanApp/post_profile_page.html', args)


@login_required(login_url='/')
def update_contact_info(request):
    if (request.method == 'POST'):
        form = EditContactInfoForm(request.POST)

        if (form.is_valid()):
            #form.save()
            user = User.objects.get(username=request.user.username)
            user.email = form.cleaned_data['email']
            user.save()
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.phone_number = form.cleaned_data['phone_number']
            user_profile.save()

            return redirect('profile_page')
    else:
        form = EditContactInfoForm()
    return render(request, 'tagpuanApp/update_contact_info.html', {'form': form})





@login_required(login_url='/')
def list_post(request):
    tags=Tag.objects.all()
    # posts=Post.objects.all()
    posts=Post.objects.filter(user=request.user)
    username = request.session.get('username')
    return render(request, 'tagpuanApp/posts.html',{'posts':posts,'username':username,'tags':tags})


@login_required(login_url='/')
def list_lost_post(request):
    tags=Tag.objects.all()
    posts=Post.objects.filter(post_type="Lost")
    username = request.session.get('username')
    return render(request, 'tagpuanApp/lostpost.html',{'posts':posts,'username':username,'tags':tags})


@login_required(login_url='/')
def list_found_post(request):
    tags=Tag.objects.all()
    posts=Post.objects.exclude(post_type="Lost")
    username = request.session.get('username')
    return render(request, 'tagpuanApp/foundpost.html',{'posts':posts,'username':username,'tags':tags})

@login_required(login_url='/')
def updatepost(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if (request.method == 'POST'):
        form = AddPostForm(request.POST or None, instance=posts)
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
        form = AddPostForm(instance=posts)
    return render(request, 'tagpuanApp/updatepost.html', {'form': form})




@login_required(login_url='/')
def deletepost(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    posts.delete()
    return redirect('home')

@login_required(login_url='/')
def filterlostpost(request, pk):
    attached=Attach.objects.filter(tag_id=pk)
    posts=Post.objects.filter(post_type="Lost")
    tags=Tag.objects.all()
    return render(request,'tagpuanApp/filterlostpost.html',{'attached':attached, 'posts':posts, 'tags':tags,'pk':pk}) 
@login_required(login_url='/')
def filterfoundpost(request, pk):
    attached=Attach.objects.filter(tag_id=pk)
    posts=Post.objects.exclude(post_type="Lost")
    tags=Tag.objects.all()
    return render(request,'tagpuanApp/filterfoundpost.html',{'attached':attached, 'posts':posts, 'tags':tags,'pk':pk})   
'''
@login_required(login_url='/')
def filterpost(request):
    form = FilterForm()
    return render(request, 'tagpuanApp/filterpost.html', {'form': form})

@login_required(login_url='/')
def list_found_post(request):
    if (request.method == 'POST'):
        form = FilterForm(request.POST)
        if (form.is_valid()):
            return redirect('filterpost')
    else:
        form = FilterForm()
        tags=Tag.objects.all()
        posts=Post.objects.exclude(post_type="Lost")
        username = request.session.get('username')
        return render(request, 'tagpuanApp/foundpost.html',{'posts':posts,'username':username,'tags':tags})
        '''