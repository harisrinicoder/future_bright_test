
from django.urls import path
from .views import course_list





urlpatterns = [
   

    # Include the blog app's URLs


     path("", course_list, name="course_list"),
     
    
]
