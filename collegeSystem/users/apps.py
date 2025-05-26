from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'collegeSystem.users'

    def ready(self):
        from . import signal  # Ensure signals are imported when the app is ready
