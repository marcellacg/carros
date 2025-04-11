from django import forms
#from cars.models import Brand, Car
from cars.models import Car

#manual
# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all()) #para mostrar a lista de opcoes no formulario
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()

#     def save(self): 
#         car = Car(
#             model = self.cleaned_data['model'], #self significando CarForm. com self ele chama a própria instancia
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save()
#         return car

#agora com ModelForm
class CarModelForm(forms.ModelForm):
    class Meta(): #reescrevendo classe
        model = Car
        fields = '__all__' #formulario relacionado ao model car. Pega todos os campos do model car (ele pega em model = Car)

    #funcao de validacao
    def clean_value(self): #usa-se clean, pois é sintaxe para validacao de campo do django
        #buscar o campo
        value = self.cleaned_data.get('value') #esse self sendo instancia do form. le-se: pegue o value deste form, pegue os dados limpos e validados, e o dado especifco que é o campo value
        if value < 20000:
            self.add_error('value', 'Valor minimo deve ser de R$20.000')
        else:
            return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não se pode cadastrar carros com fabricacao menor que 1975.')
        else:
            return factory_year