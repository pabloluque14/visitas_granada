from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Visita
from .models import Comentario
from .models import VisitaForm
from django.contrib import messages
from .serializers import VisitaSerializer, ComentarioSerializer, UserSerializer, LikeSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import requests
import json

# Create logging 
import logging
logger = logging.getLogger(__name__)


# Create your views here.

def index(request):

	lista_visitas = list(Visita.objects.all())
	# lo que le paso al template
	context = {'lista_visitas': lista_visitas}

	#print("Imprimo lista:",lista_visitas)
	return render(request, 'visitas_granada/index.html',context)

def detail_visita(request, pk):

	visita = Visita.objects.get(pk=pk)
	
	# Obtener la latitud y longitud:
	site = visita.nombre.replace(" ", "+") + "+Granada"
	uri = 'https://nominatim.openstreetmap.org/search?q={}&format=json'.format(site) 
	result = requests.get(uri)
	data = json.loads(result.text)
	lat = data[0]['lat']
	lon = data[0]['lon']

	context = {'visita': visita, 'lat': lat, 'lon': lon} 
	
		
	return render(request, "visitas_granada/detail.html", context)



def add_visita(request):
	form = VisitaForm()
	context = {'form': form}

	if request.method == 'POST':   # de vuelta con los datos

		form = VisitaForm(request.POST, request.FILES) #  bound the form

		if form.is_valid():
			form.save()
			msg = "La visita {} ha sido añadida".format(visita.nombre)
			logger.info(msg)
			return redirect('index')
			
	# GET o error	
	return render(request, "visitas_granada/add_visita.html", context)


def update_visita(request, pk):

	visita = Visita.objects.get(pk=pk)
	form = VisitaForm(instance=visita)
	context = {
		'form': form,
		'visita':visita
	
	}

	if request.method == 'POST':   # de vuelta con los datos

		form = VisitaForm(request.POST, instance=visita) #  bound the form

		if form.is_valid():
			post = form.save(commit=False)
			post.save()

			msg = "La visita {} ha sido modificada".format(visita.nombre)
			logger.info(msg)

			return redirect('index')

	else:
		form = VisitaForm(instance=visita)
			
	# GET o error	
	return render(request, "visitas_granada/update_visita.html", context)


def delete_visita(request, pk):
	visita = Visita.objects.get(pk=pk)
	visita.delete()
	msg = "La visita {} ha sido eliminada".format(visita.nombre)
	logger.info(msg)
	
	return redirect('index')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer




@csrf_exempt
def likes_endpoint(request, pk):
    try:
        visita = Visita.objects.get(pk=pk)
    except Visita.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
         serializer = LikeSerializer(visita)
         return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LikeSerializer(visita, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        