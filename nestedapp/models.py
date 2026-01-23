from django.db import models

# Create your models here.






class StdentModelClass(models.Model):

    
    sname = models.CharField(max_length=100)
    std=models.CharField(max_length=20, db_index = True)
    sub=models.CharField(max_length=50, db_index = True)



# teacher  child 
class TeacherModelClass(models.Model):

    tname= models.CharField(max_length=100)
    # sub = models.CharField(max_length=50)
    teacher = models. ForeignKey(StdentModelClass, related_name= 'teacher',  on_delete= models.CASCADE)                                 #student.teachername.all() all data fetch karvaa mate.





# all serializer fields.

class AllSerializerFieldModel(models.Model):

    gender_choice = (
        ('M', 'Male'),
        ('F','Female'),
    )

    email = models.EmailField(unique= True)                                                                #unique=true duplicate data not allowd.
    age = models.IntegerField() 
    fees = models.DecimalField(max_digits= 8, decimal_places=1)                                            # decimal_places=1   decimal pachi ek number lakvo tena mate.
    is_active = models.BooleanField(default= True)                                                         #default = true . data insert na karo to defalt true savethay.
    dob = models.DateField()
    joining_time = models.TimeField()
    gender = models.CharField(max_length= 1 , choices=gender_choice)
    created_at = models.DateTimeField(auto_now_add= True)                                                #time auto save thay. user save na kari shake.
    