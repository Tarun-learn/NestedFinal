from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from django.http import HttpResponse

from rest_framework.filters import OrderingFilter

# Create your views here.ls 

#homepae

def home(request):
    return HttpResponse("Welcome to Nested Serializer Api")

#student  get+post data
class StudentcreateApt(APIView):
    
    #show alldata
    def get (self, request):

        alldata = StdentModelClass.objects.all()
        serializer = StudentSerializer(alldata , many = True)
        return Response(serializer.data)
    
    # create data
    def post(self, request):

        serializer = StudentSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    


#teacher  get+post data
class TeacherClass(APIView):

    def get(self,request):

        alldata = TeacherModelClass.objects.all()
        serializer = TeacherSerializer(alldata, many = True)
        return Response(serializer.data)
    
    # create data
    def post(self, request):

        serializer = TeacherSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    



#all serializer field 

class AllSerializerClass(APIView):

    def get (self,request):

        alldata = AllSerializerFieldModel.objects.all()

        #sorting(ording)        # all data can sorting.   output /?sort= age
        sort_to = request.GET.get('sort')

        if sort_to:
            alldata=alldata.order_by(sort_to)


        #its a filter                                                                                                        #output . --->?age=22   !!filer ma badhi field ne aavi rete manually code lakhvo pade.
        agevariable = request.GET.get('age')                                                             #'age' is model field name     #?age__gte=18
                                                                                  
        if agevariable:
            alldata=alldata.filter(age=agevariable)

        genderv = request.GET.get('gender')

        if genderv : 
            alldata = alldata.filter(gender = genderv)


        serializer = AllSerializerField(alldata, many = True)
        return Response(serializer.data)
    
    def post(self, request):

        serializer = AllSerializerField(data = request.data)                                                               #user ee moklel data json mokliyee  for validation 
        if serializer.is_valid(): 
            serializer.save()
            return Response(
                {
                    'message': "student created suucess",
                    "data" : serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=400)
    
    

