from django import forms
from .models import BlogModel

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ('title','content')


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ('title','content')