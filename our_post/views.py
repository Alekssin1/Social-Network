from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import Post_form
from our_post.models import UserPost, PostComment
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .services import save_form_db
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from users.views import profile

User = get_user_model()

# Create your views here.
def posts(request):
    # якщо спрацьовує метод POST значить відбулося відправлення форми з додавання посту
    if request.method == "POST":
        # зберігаю значення з форми в словник
        post_form = Post_form(request.POST, request.FILES)

        if post_form.is_valid():
            save_form_db("content", request, post_form)
            return HttpResponseRedirect(request.path)
    else:

        return render(request, 'our_post\main.html', context={'form': Post_form(), 
            'posts': UserPost.objects.order_by("-id").prefetch_related('likes', 'comments', 'content').select_related('userId'), 
            "users": User.objects.all().select_related('avatar')})

def like_post(request, id):
    if request.method == "POST":
        instance = UserPost.objects.filter(id=id).select_related('userId').prefetch_related('likes', 'comments', 'content').first()
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save() 
            return render( request, 'our_post/partials/like.html', context={'post':instance})
        else:
            instance.likes.remove(request.user)
            instance.save() 
            return render( request, 'our_post/partials/like.html', context={'post':instance})


@login_required(login_url="/profile/login/")
def comments(request, post_id):
    return render(request, 'our_post\post.html', 
        context={'post': UserPost.objects.filter(id=int(post_id)).prefetch_related('comments').select_related('userId').first(),
            "users": User.objects.all().select_related('avatar')})

def del_post(request, id_post):
    user = UserPost.objects.get(id=id_post)
    UserPost.objects.filter(id=id_post).delete()
    
    return HttpResponseRedirect(reverse(profile, args=[user.userId.username]))

def del_comment(request, id_comment):    
    comment = PostComment.objects.get(id=id_comment)
    post = UserPost.objects.get(comments=comment)
    comment.delete()

    return HttpResponseRedirect(reverse(comments, args=[post.id]))
    
