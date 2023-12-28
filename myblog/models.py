from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model): 
    category = models.CharField(default="general",max_length=10, 
    choices=[
        ('sport', 'Sport'),
        ('politics', 'Politics'),
        ('economics', 'Economics'),
        ('weather', 'Weather'),
        ('health', 'Health'),
        ('education', 'Education'),
    ]
    )
    

    # Add the category dropdown field to the form

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    accuracy = models.TextField(default="true")

    # GENDER_CHOICES = [
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    # ]

    class Meta:
        ordering = ('-date_created',)

    def Count_cmnt(self):
        return self.postcomments_set.all().count()   
    
    def comments(self):
        return self.postcomments_set.all()
     
    def __str__(self):
         return self.title


class PostComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content
    


# class City(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

#         class Meta:
#             verbose_name_plural = 'cities'


