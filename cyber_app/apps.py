from django.apps import AppConfig


class CyberAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cyber_app"

    def ready(self):
        import cyber_app.signals