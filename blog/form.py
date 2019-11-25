from django import forms
from django.contrib.auth.models import User

from . models import Post, Comment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# using Post model to create form field
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

# create signup login form function
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('signup', 'Sign up', css_class="btn-primary"))
    class Meta:
        model = User
        fields = ('username', 'email', 'password', )





