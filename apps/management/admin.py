from django.contrib import admin

# Register your models here.
from .models import (
    Course,
    Teacher,
    Cycle,
    Room,
    Student,
    Subscription
)

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Cycle)

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id','name','capacity','from_hour','to_hour']
admin.site.register(Room,RoomAdmin)

admin.site.register(Subscription)