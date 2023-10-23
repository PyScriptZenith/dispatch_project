from django.contrib import admin

from dispatch.models import Dispatch, Client, Message, Logs


@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'frequency', 'status', 'client',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'dispatch',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('last_attempt', 'status','server_response', 'dispatch',)



