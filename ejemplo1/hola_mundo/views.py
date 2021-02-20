from django.shortcuts import render
from forms import LoginForm

# Create your views here.

def hola_mundo(request):
	context = {
		'nombre':'Alex',
		'edad':40,
		'materias':[
			'texting',
			'frameworks',
			'deplpyment',
			'adiministracion de proyectos'
		]
	}
	return render(request, 'hola.html', context)

def ingenieria(request):
	context = {}
	form = LoginForm
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			context['ok'] ='ok'
		context['ok'] = 'Error de validacion'

	context['form'] = form	
	return render(request,'ingenieria.html',context)