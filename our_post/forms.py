from django import forms

from our_post.models import UserPost
from .models import *

# модель пост
class Post_form(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"post_input form-control", "placeholder":"Текст посту...", "id":"post_input", 
        "type":"text", "rows":"2"}), label="")
    content = forms.ImageField(widget=forms.HiddenInput(attrs={"class":"my_photos_post", "type":"file", "multiple":"multiple",
             "accept":"image/png, image/jpeg, image/jpg", "id":"file"}), label="", required=False)
    class Meta:
        model = UserPost
        fields = ("message",)

# class Like_form(forms.ModelForm):
    