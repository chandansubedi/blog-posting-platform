from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model): 
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

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
    

