from django.urls import path
from . import views
urlpatterns = [
    path('', views.posts, name='our_post'),
    path('like/<int:id>', views.like_post, name='like_post'),
    path('comments/<post_id>', views.comments, name='comments'),  
]

