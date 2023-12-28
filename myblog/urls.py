from django.urls import path 
from .import views
urlpatterns =[
    path('',views.ShowBlogs, name='ShowBlogs'),
    path('post_details/<int:pk>/', views.Post_details , name='post_details'),
    path('post_category_sport/', views.Post_category_sport , name='post_category_sport'),
    path('post_category_politics/', views.Post_category_politics , name='post_category_politics'),
    path('post_category_weather/', views.Post_category_weather , name='post_category_weather'),
    path('post_category_health/', views.Post_category_health , name='post_category_health'),
    # path('weather/', views.Most_commented_posts , name='weather'),
    # path('post_category_politics/', views.Post__category_politics , name='post_category_politics'),
    # path('post_details/<int:pk>/', views.Post_details , name='post_details'),
    # path('MarqueeNdetails/<int:pk>/', views.MarqueeNdetails , name='MarqueeNdetails'),
    path('edit_post/<int:pk>/', views.edit_post , name='edit_post'),
    path('delete_post/<int:pk>/', views.Delete_post , name='delete_post'),
    path('search/', views.Search, name='search'),
]