from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__ (self):
        return self.name


class Car(models.Model):  # tabela car no banco de dados
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=100, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # subscreve-se função padrão do Model
    def __str__(self):
        return self.model

#classes para o inventário da aplicação
#assim que atualizamos esse arquivo, rodar o makemigrations

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: #subscrevendo meta
        ordering = ['-created_at'] #para ordernar descrescente

    def __str__(self):
        return f'{self.cars_count} - {cars_value}'
