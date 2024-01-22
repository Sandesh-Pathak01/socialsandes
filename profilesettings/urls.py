from django.urls import path
from . import views

urlpatterns = [
    path('userprofile', views.logged_user_profile, name='profile'),
    path('settings/', views.profile_settings, name='settings'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('edit_profile/', views.edit_profile, name='profile_edit'),
    path('profiles/<user>', views.other_profiles, name='other_users'),
    path('likes/', views.likes_profile, name='likes_profile'),
    path('commentss/', views.comments_profile, name='pcomments'),
    path('profile/<int:profile_id>/follow/', views.follow_profile, name='follow_profile'),
    path('profile/<int:profile_id>/unfollow/', views.unfollow_profile, name='unfollow_profile'),
]