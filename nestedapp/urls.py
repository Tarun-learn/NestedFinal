from django.urls import path
from .views import *



urlpatterns=[

    path('student/',StudentcreateApt.as_view()),
    path('teacher/',TeacherClass.as_view()),
    path('allser/', AllSerializerClass.as_view()),
    
   
]