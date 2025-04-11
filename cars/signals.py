from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory

@receiver(pre_save, sender=Car) #receive ouve tudo o que acontece na tabela de carros no evento pre_save
def car_pre_save(sender, instance, **kwargs): #sender é o 'enviador' que esta mandando esse evento para o signal, sender é o model car 
    #verificar se a bio foi informada, se não, criar uma automatica
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente!'

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate( #campo personalizado
        total_value=Sum('value') #somando todos os values dos registros de carros
    )['total_value'] #o aggregate retorna um dic, entao pegamos so o valor
    CarInventory.objects.create( #criar registro novo na tabela logo em seguida
        cars_count=cars_count, #esses sendo os dados
        cars_value=cars_value
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs):
#     print('### pre delete ###')

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()