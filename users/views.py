from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

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

    data = {
        "author": userProfile,
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