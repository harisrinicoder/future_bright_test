
from django.urls import path
# from .views import blog_home


from . import views



urlpatterns = [
   

    # Include the blog app's URLs


    #  path("", blog_home, name="blog_home"),


         path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    
]
