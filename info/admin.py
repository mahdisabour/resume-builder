from django.contrib import admin

from .models import PersonalInfo, Owner, Resume, EmploymentHistory, Education, WebsiteAndSocialMedia, skill, language, course


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'firstName', 'lastName', "phone"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['userId']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'resumeTitle', 'owner']


@admin.register(EmploymentHistory)
class EmploymentHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(WebsiteAndSocialMedia)
class WSAdmin(admin.ModelAdmin):
    pass


@admin.register(skill)
class skillAdmin(admin.ModelAdmin):
    pass


@admin.register(language)
class languageAdmin(admin.ModelAdmin):
    pass


@admin.register(course)
class courseAdmin(admin.ModelAdmin):
    pass