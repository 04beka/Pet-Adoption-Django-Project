from django.apps import App, AppConfig

class PetsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pets"

    def ready(self):
        from . import signals  # noqa

