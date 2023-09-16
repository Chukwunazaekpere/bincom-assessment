from django.apps import AppConfig


class PollingUnitsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polling_units'
    class Meta:
        verbose_name = "Polling unit"
        verbose_name_plural = "Polling units"
