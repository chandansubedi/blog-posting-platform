from django import forms
from .models import BlogModel,PostComments
# from django.forms import ModelForm,TextInput,fields,widgets
class BlogModelForm(forms.ModelForm):
    CATEGORIES_CHOICES = [
        ('sport', 'Sport'),
        ('politics', 'Politics'),
        ('economics', 'Economics'),
        ('weather', 'Weather'),
        ('health', 'Health'),
        ('education', 'Education'),
    ]
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    category = forms.ChoiceField(choices=CATEGORIES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = BlogModel
        fields = ('title','content','category')


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


# class CityForm(ModelForm):
#     class Meta:
#         Model = City
#         fieldS =['name']
#         widgets = {
#             'name' :TextInput(attrs={'class':'input' , 'placeholder':'City Name'}),
#         }
