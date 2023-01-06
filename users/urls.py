from django.urls import path
from . import views
urlpatterns = [
 #  сторінка з можливостю реєстрації, виходу з облікового запису та створення облікового запису
 path('', views.home, name="home_home"),
 
 #  сторінка реєстрації
 path("signup/", views.SignUp.as_view(), name="signup"),
 
 path("profile/<str:username>/", views.profile, name="profile"),
 
 path("followToggle/<str:author>/",views.followToggle, name="followToggle")
]