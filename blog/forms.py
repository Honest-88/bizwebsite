from django import forms
from .models import Post, Comment
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 
        'category', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your comment here ...', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)





#class CommentForm(forms.ModelForm):
#    content = forms.CharField(widget=forms.Textarea(attrs={
#        'class': 'form-control',
#        'placeholder': 'Type your comment',
#        'id': 'usercomment',
#        'rows': '4'
#    }))
#    class Meta:
#        model = Comment
#        fields = ('content', )