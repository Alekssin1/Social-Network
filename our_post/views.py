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
from django.views import View
from django.views.generic.detail import DetailView

User = get_user_model()

class Post(View):
    def post(self, request, *args, **kwargs):
        post_form = Post_form(self.request.POST, self.request.FILES)

        if post_form.is_valid():
            save_form_db("content", self.request, post_form)
            return HttpResponseRedirect(self.request.path)
        
    def get(self, request, *args, **kwargs):
        return render(request, 'our_post\main.html', context={'form': Post_form(), 
            'posts': UserPost.objects.order_by("-id").prefetch_related('likes', 'comments', 'content').select_related('userId'), 
            "users": User.objects.all().select_related('avatar')})

class Like_post(DetailView):
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
        instance = UserPost.objects.filter(id=self.kwargs.get("id")).select_related('userId').prefetch_related('likes', 'comments', 'content').first()
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
    
