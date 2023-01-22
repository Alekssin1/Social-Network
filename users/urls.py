from django.urls import path
from . import views
urlpatterns = [
 #  сторінка з можливостю реєстрації, виходу з облікового запису та створення облікового запису
 path('', views.Home.as_view(), name="home_home"),
 
 #  сторінка реєстрації
 path("signup/", views.SignUp.as_view(), name="signup"),
 
 path("search/", views.Search.as_view(), name="search"),
 
 path('edit/<str:username>/', views.Edit_profile.as_view(), name="edit_profile"),
 
 path("followToggle/<str:username>/",views.Follow_user.as_view(), name="followToggle"),
 
 path("<str:username>/", views.Profile.as_view(), name="profile"),
]