from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('aboutus/', views.about, name='blog-about'),
    path('login/', views.user_login, name='blog-login'),
    path('login-verify/', views.user_login_verify, name='blog-login-verify'),
    path('logout/', views.user_logout, name='blog-logout'),
    path('create-post-form/', views.create_post_form, name='create-post-form'),
    path('create-post/', views.create_post, name='create-post'),
    path('edit-post-form/<int:id>', views.edit_post_form, name='edit-post-form'),
    path('edit-post/', views.edit_post, name='edit-post'),
    path('delete-post-form/<int:id>', views.delete_post_form, name='delete-post-form'),
    path('delete-post/', views.delete_post, name='delete-post'),
    path('profile/', views.profile, name='user-profile'),
]
