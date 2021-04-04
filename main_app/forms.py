from django import forms

from .models import Post, Comment

# added a postform
class PostForm(forms.ModelForm):
    # meta class beacuse that's how django can do it
    class Meta:
        # which model
        model = Post
        fields = ['title', 'content']

# added a commentform
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

