from django.apps import AppConfig


class DisasterAppConfig(AppConfig):
    name = 'disaster_app'

    def ready(self):
        print("Scheduling API fetch operation.")
        from .fetch_scheduler import fetch_updater
        fetch_updater.start()
