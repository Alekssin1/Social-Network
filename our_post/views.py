from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import Post_form
from our_post.models import UserPost, PostComment, Photo 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .services import save_form_db

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

        return render(request, 'our_post\main.html', context={'form': Post_form(), 'posts': UserPost.objects.order_by("-id")})

def like_post(request, id):
    if request.method == "POST":
        instance = UserPost.objects.get(id=id)
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
    return render(request, 'our_post\post.html', context={'post': UserPost.objects.get(id=int(post_id))})
