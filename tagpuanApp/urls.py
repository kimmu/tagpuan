from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('profile/home/', views.home, name="home"),
    path('profile/add_post/', views.add_post, name="addpost"),
    path('profile/user/', views.profile_page, name="profile_page"),
    path('profile/user/update_contact_info/', views.update_contact_info, name="update_contact_info"),
    path('register/user_profile/', views.create_userprofile, name="userprofile"),
    path('posts',views.list_post, name="list_post"),
    path('lostpost',views.list_lost_post, name="list_lost_post"),
    path('foundpost',views.list_found_post, name="list_found_post"),
    path('updatepost/<int:pk>/',views.updatepost, name='updatepost'),
    path('deletepost/<int:pk>/',views.deletepost, name='deletepost'),
	path('postdelete/',views.postdelete, name='postdelete'),
	path('lostdelete/',views.lostdelete, name='lostdelete'),
	path('founddelete/',views.founddelete, name='founddelete'),
	path('userprofile/<int:pk>/',views.post_profile_page,name='post_profile_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)