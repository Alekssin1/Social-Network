from django import template
from our_post.models import UserPost

register = template.Library()

@register.simple_tag()
def getPostUser(id):
    return UserPost.objects.filter(userId=id).order_by("-id")

@register.simple_tag()
def getCountPostUser(id):
    return UserPost.objects.filter(userId=id).count()