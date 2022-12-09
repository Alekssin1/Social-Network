from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# рендер сторінки з можливостю реєстрації, виходу з облікового запису та створення облікового запису
def home(request):
    return render(request, "users/home.html")

# відмалювання регістрації 
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"