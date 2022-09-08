from django.contrib import admin
from .models import *
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('signup','Title', 'Content', 'UpdationDate')
    list_filter = ('UpdationDate',)

admin.site.register(Signup)
admin.site.register(Notes, NotesAdmin)