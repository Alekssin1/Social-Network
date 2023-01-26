from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import Post_form
from our_post.models import UserPost, PostComment
from django.http import HttpResponseRedirect
from .services import save_form_db
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

User = get_user_model()

class Post(View):
    def post(self, request, *args, **kwargs):
        post_form = Post_form(self.request.POST, self.request.FILES)

        if post_form.is_valid():
            save_form_db("content", self.request, post_form)
            return HttpResponseRedirect(self.request.path)
        
    def get(self, request, *args, **kwargs):
        userProfile = User.objects.filter(username=self.request.user.username).select_related('avatar')[0]
        followers = userProfile.followers.select_related('avatar')
        # followers |= UserPost.objects.filter(userId=userProfile)

        return render(request, 'our_post\main.html', context={'form': Post_form(),
            'posts': UserPost.objects.order_by("-id").prefetch_related('likes', 'comments', 'content').select_related('userId', 'userId__avatar')\
                .only('userId', 'userId__username', 'userId__avatar__avatar', 'message', 'content', 'createdAt', 'comments', 'likes', 'userId__is_superuser'), 
            "users": User.objects.all().select_related('avatar').only('avatar__avatar'), "posts_following": UserPost.objects.filter(userId__in=followers).order_by("-id").prefetch_related('likes', 'comments', 'content').select_related('userId', 'userId__avatar')\
                .only('userId', 'userId__username', 'userId__avatar__avatar', 'message', 'content', 'createdAt', 'comments', 'likes', 'userId__is_superuser')|UserPost.objects.filter(userId=userProfile).order_by("-id").prefetch_related('likes', 'comments', 'content').select_related('userId', 'userId__avatar')\
                .only('userId', 'userId__username', 'userId__avatar__avatar', 'message', 'content', 'createdAt', 'comments', 'likes', 'userId__is_superuser') })

class Like_post(DetailView):
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
        instance = UserPost.objects.filter(id=self.kwargs.get("id")).select_related('userId').prefetch_related('likes', 'comments', 'content', 'comments__userId__avatar')\
            .only('userId', 'userId__username', 'userId__avatar__avatar', 'message', 'content', 'createdAt', 'comments', 'likes', 'userId__is_superuser').first()
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save() 
            return render( request, 'our_post/partials/like.html', context={'post':instance})
        else:
            instance.likes.remove(request.user)
            instance.save() 
            return render( request, 'our_post/partials/like.html', context={'post':instance})
        
class Comments(LoginRequiredMixin, DetailView):
    model = UserPost
    template_name = 'our_post\post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        return UserPost.objects.filter(id=int(self.kwargs.get("post_id")))\
            .prefetch_related('comments', 'comments__userId__avatar').select_related('userId')\
            .only('userId__is_superuser', 'userId__id', 'userId', 'userId__username', 'message', 'content', 'comments', 'createdAt', 'id').first()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all().select_related('avatar').only('username', 'is_superuser', 'avatar__avatar')
        return context
    
class Delete_post(DeleteView):
    model = UserPost
    pk_url_kwarg = 'id_post'
    
    def get(self, request, *args, **kwargs):
        user = UserPost.objects.get(id=self.kwargs.get('id_post'))
        UserPost.objects.filter(id=self.kwargs.get('id_post')).delete()
        return HttpResponseRedirect(reverse('profile', args=[user.userId.username]))
    
class Delete_comment(DeleteView):
    pk_url_kwarg = 'id_comment'
    
    def get(self, request, *args, **kwargs):
        comment = PostComment.objects.get(id=self.kwargs.get('id_comment'))
        post = UserPost.objects.get(comments=comment)
        comment.delete()

        return HttpResponseRedirect(reverse('comments', args=[post.id])) 
