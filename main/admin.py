from django.contrib import admin
from .models import Project, Skill, Education, ContactMessage, Appointment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ('title','summary')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name','level','order')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree','institution','start_year','end_year')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at','processed')
    list_filter = ('processed',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'start', 'end', 'confirmed')
    list_filter = ('confirmed',)
    search_fields = ('name', 'email')
