from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created', 'about')
    list_filter = ('title', 'date')

admin.site.register(Evento, EventAdmin)