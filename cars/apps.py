from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    #reescrevendo funcao ready
    def ready(self): #para inicializacao da aplicacao
        import cars.signals
