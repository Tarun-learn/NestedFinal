from rest_framework import serializers
from .models import *





#childs 

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherModelClass
        # fields = '__all__'                        # id,name.sub,student from teacherclass
        fields = ['tname','teacher']                       #show onlly tname in


#parentserializer
class StudentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many = True, read_only = True)
    class Meta:
        model = StdentModelClass
        fields = '__all__'         # teacher property and sub



class AllSerializerField(serializers.ModelSerializer):

    class Meta:
        model = AllSerializerFieldModel
        # fields = [
        #     'email',
        #     'age',
        #     'fees',
        #     'is_active',
        #     'dob',
        #     'joining_time',
        #     'gender',
        #     'created_at',
        
        # ]
        fields = '__all__'
 
    def to_representation(self, instance):                                                                #to_representation=> database ma changes karaya vagar field add kari shakay ane output ma joi shakay.
        data =  super().to_representation(instance)
    
        #custom output. 
        data ['status'] = "Active"  if instance.is_active else "Inactive"
        data ['fees_in_rupees'] = f"$ {instance.fees}"
        data ['gender_full'] = "Male" if instance.gender =='M' else "Female"

        email = instance.email
        data ['hide_mail'] = email[:2] + "***@" + email.split("@")[1]



        return data