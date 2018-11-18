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
    path('register/user_profile/', views.create_userprofile, name="userprofile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)