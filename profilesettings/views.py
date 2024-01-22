from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from . import models as data
from django.db import transaction
from django.contrib import messages
from home.models import Post, Comment

# Create your views here.
def profile_settings(request):
    details = data.Profile.objects.get(user=request.user)
    context = {
        'data': details,
    }

    return render(request, 'settings.html', context)


def profile_update(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                user_profile = data.Profile.objects.get(user=request.user)

                user_profile.name = request.POST.get('name')
                user_profile.email = request.POST.get('email')
                user_profile.dob = request.POST.get('dob')
                user_profile.gender = request.POST.get('gender')
                if request.FILES.get('profile_picture'):
                    user_profile.profile_pic = request.FILES.get('profile_picture')

                user_profile.save()  

                messages.info(request, 'Profile updated successfully')
                return redirect('settings')  
        except Exception as e:
            messages.error(request, f'Error updating profile: {e}')
            return HttpResponse('Hello')
        

def logged_user_profile(request):
    
    user_profile = data.Profile.objects.get(user=request.user)
    user_posts = data.postmodel.Post.objects.filter(user=request.user)
    
    context = {
        'data': user_profile,
        'post': user_posts,
        'is_following': user_profile.is_following(request.user),
        'followers_count': user_profile.followers_count(),
        'following_count': user_profile.following_count(),
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        try:
            user_profile = data.Profile.objects.filter(user=request.user)
            data_dict = {
                'name': request.POST.get('name'),
                'bio': request.POST.get('bio'),
            }
            user_profile.update(**data_dict)
            messages.info(request, 'Profile Updated Successfully')

        except Exception as e:
             messages.error(request, f'Error updating profile: {e}')

        return redirect('profile')
    else:
        return HttpResponse('Not Found!')
    

# def other_profiles(request, user):
#     user_profile = data.Profile.objects.get(user__username=user)
#     user_posts = data.postmodel.Post.objects.filter(user__username=user)
    
#     context = {
#         'data': user_profile,
#         'post': user_posts,
#     }
#     if user_profile.user == request.user:
#         return redirect('profile')
#     return render(request, 'profile.html', context)
    

def other_profiles(request, user):
    user_profile = get_object_or_404(data.Profile, user__username=user)
    user_posts = data.postmodel.Post.objects.filter(user__username=user)

    context = {
        'data': user_profile,
        'post': user_posts,
        'is_following': user_profile.is_following(request.user),
        'followers_count': user_profile.followers_count(),
        'following_count': user_profile.following_count(),
    }

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'follow':
            user_profile.follow(request.user)
        elif action == 'unfollow':
            user_profile.unfollow(request.user)

    if user_profile.user == request.user:
        return redirect('profile')

    return render(request, 'profile.html', context)

def follow_profile(request, profile_id):
    profile = get_object_or_404(data.Profile, pk=profile_id)
    profile.follow(request.user)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def unfollow_profile(request, profile_id):
    profile = get_object_or_404(data.Profile, pk=profile_id)
    profile.unfollow(request.user)
    return redirect(request.META.get('HTTP_REFERER', '/'))



def likes_profile(request):
    if request.method == 'POST':
        user = request.user
        post_id = request.POST.get('post_id')

        post_instance = Post.objects.get(post_id=post_id)
        if post_instance.likes.filter(id=user.id).exists():
            post_instance.likes.remove(user)
        else:
            post_instance.likes.add(user)

        return redirect(request.META.get('HTTP_REFERER', '/'))
    

def comments_profile(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment = request.POST.get('comment')
        post_instance = Post.objects.get(post_id=post_id)

        new_comment = Comment.objects.create(
            post_comment = post_instance,
            name=request.user,
            comment = comment
        )
        new_comment.save()

        return redirect(request.META.get('HTTP_REFERER', '/'))




        





