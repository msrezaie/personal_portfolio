from django.contrib import admin
from . models import Project, Tag, Profile, Skill, Page, Contact

admin.site.register(Page)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Skill)

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'name', 'title', 'email', 'message')

