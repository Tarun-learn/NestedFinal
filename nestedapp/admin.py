from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(StdentModelClass)
admin.site.register(TeacherModelClass)
admin.site.register(AllSerializerFieldModel)