from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, AvatarUserForm, BackgroundForm
from django.db.models import Q
from chats.models import ChatModel

from users.forms import CustomUserCreationForm

User = get_user_model()
# рендер сторінки з можливостю реєстрації, виходу з облікового запису та створення облікового запису
def home(request):
    return render(request, "users/home.html")

# відмалювання регістрації 
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
    
def profile(request, username):
    userProfile = User.objects.get(username=username)
    form = UserProfileForm()
    form_avatar = AvatarUserForm()
    form_background = BackgroundForm()
    data = {
        "author": userProfile,
        "form": form,
        "form_avatar": form_avatar,
        "form_background": form_background,
    }
    return render(request, "users/profile.html", data)


def followToggle(request, username):
    authorObj = User.objects.get(username=username)
    currentUserObj = User.objects.get(username=request.user.username)
    following = authorObj.following.all()

    if username != currentUserObj.username:
        if currentUserObj in following:
            authorObj.following.remove(currentUserObj.id)
        else:
            authorObj.following.add(currentUserObj.id)

    return HttpResponseRedirect(reverse(profile, args=[authorObj.username]))

def edit_profile(request, username):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        form_avatar = AvatarUserForm(request.POST, request.FILES)
        form_background = BackgroundForm(request.POST, request.FILES)
        new_username = username
        
        if form.is_valid():
            new_username = form.cleaned_data['username']
            if new_username:
                if new_username == username: 
                    User.objects.filter(username=username).update(username='')
                    User.objects.filter(username='').update(username=new_username)
                else:
                    User.objects.filter(username=username).update(username=new_username)
                    ChatModel.objects.filter(sender=username).update(sender=new_username)
        if form_avatar.is_valid() and form_background.is_valid():
            if form_avatar.cleaned_data['avatar']:
                avatar = form_avatar.save()
                if new_username:
                    User.objects.filter(username=new_username).update(avatar=avatar)
                else:
                    User.objects.filter(username=username).update(avatar=avatar)
            if form_background.cleaned_data['background']:
                background = form_background.save()
                if new_username:
                    User.objects.filter(username=new_username).update(background=background)
                else:
                    User.objects.filter(username=new_username).update(background=background)
        return HttpResponseRedirect(reverse(profile, args=[new_username]))
    
            
def search(request):
    if request.method == "POST":
        query = request.POST.get('q')
        object_list = User.objects.filter(
            Q(username__icontains=query)
        )
    return render( request, 'partials/search.html', context={'search_users':object_list})