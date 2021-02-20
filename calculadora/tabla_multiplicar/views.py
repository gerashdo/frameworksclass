from django.shortcuts import render
from .forms import TablaForm

def tabla_multiplicar(request):
    context = {}
    form = TablaForm
    if request.method == 'POST':
        form = TablaForm(request.POST)
        if form.is_valid:
            context['numero'] = form['numero'].data
            num = int(form['numero'].data)
            lista = []
            for indice in range(1,101):
                lista.append(indice*num)
            context['lista'] = lista
    context['form'] = form
    return render(request,'tabla_multiplicacion.html',context) 
