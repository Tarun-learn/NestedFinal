from django.urls import path
from .views import *



urlpatterns=[

    path('student/',StudentcreateApt.as_view(), name = "student"),
    path('teacher/',TeacherClass.as_view(), name = 'teacher'),
    path('allser/', AllSerializerClass.as_view(), name = 'allser'),
    
    
   
]