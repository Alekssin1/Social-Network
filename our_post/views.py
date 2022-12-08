from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import Post_form
from chats.models import Photo, UserPost, PostLikes
from django.http import HttpResponseRedirect, JsonResponse

User = get_user_model()


# Create your views here.
def posts(request):
    all_user = User.objects.all()
    if request.method == "POST":
        post_form = Post_form(request.POST, request.FILES)

        if post_form.is_valid():
            temp = post_form.save(commit=False)
            temp.userId = request.user
            post_form.cleaned_data
            temp.save()

            for i in request.FILES.getlist("content"):
                temp.content.add(Photo.objects.create(photo=i))
            temp.save()
            return HttpResponseRedirect(request.path)
    else:
        id_post_like = []
        all_like = {}
        my_like = {}
        try:
            all_like_post = PostLikes.objects.all()
            like_this_user = PostLikes.objects.filter(userId_id=request.user)
            for i in like_this_user:
                id_post_like.append(i.postId_id)

            for like in all_like_post:
                if all_like.get(like.postId_id, False):
                    all_like[like.postId_id].append(like.userId_id)
                else:
                    all_like[like.postId_id] = [like.userId_id]

            for key, value in all_like.items():
                my_like[key] = len(value)

        except Exception:
            pass

        post_form = Post_form()
        return render(request, 'main.html', context={'form': post_form, 'posts': UserPost.objects.order_by("-id"), 'like_posts': id_post_like, 'number_like': my_like, 'all_id_post': list(my_like.keys())})


def like(request):
    post_id = request.GET.get('result', False)
    data = {"like": False}
    temp = True

    try:
        my_like = PostLikes.objects.get(
            postId_id=int(post_id), userId_id=request.user)
    except Exception:
        temp = False

    if post_id and not temp:
        my_user = UserPost.objects.get(id=int(post_id))
        post_like = PostLikes()
        post_like.userId = request.user
        post_like.postId = my_user
        post_like.save()
        data = {"like": True}
        return JsonResponse(data)

    if temp:
        my_like.delete()

    return JsonResponse(data)


def comments(request, post_id):

    return render(request, 'post.html', context={'posts': UserPost.objects.get(id=int(post_id)), })
