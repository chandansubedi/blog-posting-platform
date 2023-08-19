from django import forms
from .models import BlogModel,PostComments

class BlogModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = BlogModel
        fields = ('title','content')


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ('title','content') 

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))
    class Meta:
        model = PostComments
        fields = ('content',)
