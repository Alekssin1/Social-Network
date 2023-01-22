from django.urls import path
from . import views
urlpatterns = [
    path('', views.Post.as_view(), name='our_post'),
    path('like/<int:id>', views.Like_post.as_view(), name='like_post'),
    path('comments/<post_id>', views.Comments.as_view(), name='comments'), 
    path('delete/comment/<int:id_comment>/', views.del_comment, name='delete_comment'),
    path('delete/<int:id_post>/', views.Delete_post.as_view(), name='delete'),
]

