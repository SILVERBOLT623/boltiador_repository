from django.contrib import admin
from .models import Profile, Skill, Project, Education, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline', 'email']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['order', 'proficiency']
    list_filter = ['category']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_editable = ['featured', 'order']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_year', 'end_year', 'order']
    list_editable = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'sent_at', 'is_read']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'sent_at']
