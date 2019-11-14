from django import forms
from . models import Post

# using Post model to create form field
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


