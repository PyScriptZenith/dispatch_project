from django.contrib import admin

from dispatch.models import Dispatch, Client


@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = ('time', 'frequency', 'status', 'client',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name',)

