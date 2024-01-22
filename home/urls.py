from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_posts', views.upload_posts, name='upload_posts'),
    path('like/', views.likes_home, name='hlikes'),
    path('comment/', views.comments_home, name='hcomments'),
    path('deletepost/<post_id>/', views.delete_post, name='delete_post'),
    path('search/', views.search_page, name='search_page')
]