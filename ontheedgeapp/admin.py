from django.contrib import admin
from .models import ResultCategory, TaskCategory, \
    Item, Task, Inspection, PicRecord, Grade

admin.site.register(ResultCategory)
admin.site.register(TaskCategory)
admin.site.register(Item)
admin.site.register(Grade)
admin.site.register(Task)
admin.site.register(Inspection)
admin.site.register(PicRecord)