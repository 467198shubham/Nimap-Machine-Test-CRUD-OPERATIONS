from django.contrib import admin
from .models import User
from .models import Projects

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','clientname')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display=('id','projectname')
    
    