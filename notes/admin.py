from django.contrib import admin

from .models import Note

@admin.register(Note)   #register Note
class NoteAdmin(admin.ModelAdmin):
    pass
