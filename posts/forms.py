from django import forms
#from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from .models import Post, Comment



class TinyMCEWidget(TinyMCE):
	def use_required_attribute(self, *args):
		return False


class PostForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title','overview','content','thumbnail','categories','featured','previous_post','next_post')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
     }))
    class Meta:
        model = Comment
        fields = ('content',)
        
