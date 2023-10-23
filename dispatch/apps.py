from django.apps import AppConfig

from time import sleep


class DispatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dispatch'

    def ready(self):
        from jobs import updater
        sleep(2)
        updater.start()
