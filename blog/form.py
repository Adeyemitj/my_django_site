from django import forms
from . models import Post, Comment

# using Post model to create form field
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'text', }



