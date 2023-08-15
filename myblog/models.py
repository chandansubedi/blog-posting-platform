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
    
    def __str__(self):
         return self.title


