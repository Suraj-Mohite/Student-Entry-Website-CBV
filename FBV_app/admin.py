from FBV_app.models import User
from django.contrib import admin

# Register your models here.

@admin.register(User)
class adminUserModel(admin.ModelAdmin):
    list_display=['id','name','email','mob_number','image']