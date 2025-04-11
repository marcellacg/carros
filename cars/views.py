#from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# def car_views(request): #request tem todos os dados da requisicao que o usuario ta fazendo
#     #print(request.GET.get('search')) tendo na url o endpoint ?search=Teste, ele devolte Teste no terminal.
#     #basicamente a gnt navega na requisicao do usuario, buscando os dados que ele envia.
#     # com ?search=Teste&nome=pycodebr, ele devolve um dicionario
#     cars = Car.objects.all()
#     search = request.GET.get('search')

#     #usuario passa parametro no search ele vai retornar o que ha no banco
#     #usuario nao passa parametro, entao a aplicacao devolve a lista de todos os carros
    
#     if search: #se a variavel contem alguma coisa
#         cars = cars.filter(model__icontains=search) #filtrar por marca, indo por id pois é chave estrangeira e Fiat tá setado como 1
#         print(cars)
#     #por nome seria brand__name = 'Fiat' e com dois underlines, pois ele vai atras da propriedade em outra tabela
#     #com model__contains = 'Fiat' ele vai procurar o que contém Fiat, nao somente estritamente Fiat. É uma funcao ja embutida

#     #ha tbm o contains com i (icontais) de ignore case, que ignora caixa alta, baixa, camel case, etc

#     #ha o order_by para ordernar por modelo, por exemplo. cars = Car.objects.all().order_by('model') o ('-model') inverte a ordem

#     #return render(request, 'cars.html') # com django template há uma terceiro parametro, de contexto
#     # return render(request, 'cars.html', {'cars': {'model': 'Astra 2.0'}})
#     return render(
#         request, 
#         'cars.html',
#         {'cars' : cars}
#     )


# class CarsView(View):

#     def get(self, request):
#         cars = Car.objects.all().order_by('model')
#         search = request.GET.get('search')

#         if search:
#             cars = cars.filter(model__icontains=search)

#         return render(
#             request,
#             'cars.html',
#             {'cars': cars}
#         )

#_________com ListView_________
class CarsListView(ListView):
    model = Car #Car.objects.all()
    template_name = 'cars.html'
    context_object_name = 'cars'
    #o default do queryset() é all, por isso ele ja pega do model de ListView
    def get_queryset(self): #subscrevendo queryset
        cars = super().get_queryset().order_by('model') #filtrar
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

# def new_car_view(request):
#     if request.method == 'POST': #criando registro de carros assim que clica no submit
#         new_car_form = CarModelForm(request.POST, request.FILES) #request.POST pega os dados da requisicao enviada, request.FILES que é incluindo arquivos

#         #validacao
#         if new_car_form.is_valid(): #aqui ele vai ate o forms pra ir atrás das validacoes. com tudo ok ele persiste no banco, senao, nao
#             new_car_form.save() #funcao save diretamente do forms.Ela instancia o obj Car com os dados do form e salva com o save() do banco de dados
#             return redirect('cars_list') #redireciono para lista de carros

#     else:
#         new_car_form = CarModelForm() #essa e a linha seguinte retornam o form vazio
#     return render(request, 'new_car.html', {'new_car_form' : new_car_form})

# class NewCarView(View):

#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, 'new_car.html', {'new_car_form' : new_car_form})

#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, 'new_car.html', {'new_car_form' : new_car_form}) #se n cair no if, o retorno é o formulario renderizado com os erros na tela
        
@method_decorator(login_required(login_url='login'), name='dispatch') #o decorator (camada de proteçao) vai executar a função login_required antes de executar a view
#sem o parametro login_url='login', o django redireciona para accounts/login como default, entao sinalizamos ja no parametro qual é a url da aplicacao
#o dispatch sera o primeiro executado para verificar alguns dados basicos da sessao, como metodos get/post/update/delete, body, etc
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/' #manda usuario para a pág de lista de carros


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm #o django traz o form preenchido pro usuario editar
    template_name = 'car_update.html'
    #success_url = '/cars/' #nessa url o usuário é levado para a listagem de carros
    #sobrescrevendo o metodo para que ele seja direcionado para o carro especifico:
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk}) #kwargs é o argumento que vai passar na url que ta em urls, e que foi definida a partir do pk do objeto carro
    #usa-se kwargs porque é requerido. o parametro é tipo str, sendo viavel aqui um dicionario

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
