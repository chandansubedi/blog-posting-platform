from django.contrib import admin
from .models import BlogModel,PostComments
# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title','date_created')
    




admin.site.register(BlogModel,BlogModelAdmin)
admin.site.register(PostComments)
