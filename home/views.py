from django.shortcuts import render, HttpResponse, redirect
from . import models as data
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Home Page
@login_required
def home(request):

    all_posts = data.Post.objects.all()
    user_pfp = data.Profile.objects.get(user=request.user)

    context = {
        'data': all_posts,
        'user_pfp': user_pfp,
    }

    return render(request, 'home.html', context)


# Uploading Posts
@login_required
def upload_posts(request):
    if request.method == 'POST':
        user_profile = data.Profile.objects.get(user=request.user)

        with transaction.atomic():
            new_post = {
                'user': request.user,
                'profile_pic': user_profile,
                'name': user_profile,
                'caption': request.POST.get('caption'),
            }

            post_image = request.FILES.get('post_image')
            if post_image:
                new_post['post_image'] = post_image

            data.Post.objects.create(**new_post)

        return redirect('home')

    return render(request, 'your_template.html')


def likes_home(request):
    if request.method == 'POST':
        user = request.user
        post_id = request.POST.get('post_id')

        post_instance = data.Post.objects.get(post_id=post_id)
        if post_instance.likes.filter(id=user.id).exists():
            post_instance.likes.remove(user)
        else:
            post_instance.likes.add(user)

        return redirect('home')
    

def comments_home(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment = request.POST.get('comment')
        post_instance = data.Post.objects.get(post_id=post_id)

        new_comment = data.Comment.objects.create(
            post_comment = post_instance,
            name=request.user,
            comment = comment
        )
        new_comment.save()

        return redirect('home')


def delete_post(request, post_id):
    post_instance = data.Post.objects.get(post_id=post_id)
    post_instance.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def search_page(request):
    context = {}
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            search_results = data.Profile.objects.filter(Q(name__icontains=search) | Q(user__username__icontains=search))
            context = {
                'search': search_results,
            }
        else:
            context = {
                'search': None,
            }
    return render(request, 'search.html', context)