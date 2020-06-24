from django.shortcuts import render, HttpResponse, redirect
from .models import AcumuladoNacional

def index(request):
    lista_covid = AcumuladoNacional.objects.all()
    lista_meses =[]
    lista_cont =[]
    lista_fall =[]
    for datos in lista_covid:
      lista_meses.append(datos.mes)
      lista_cont.append(datos.contagiados)
      lista_fall.append(datos.fallecidos)            
    context = {'meses': lista_meses,'contagiados': lista_cont,'fallecidos':lista_fall}
    return render(request,'index.html',context)

def regiones(request):
    return render(request,'regiones.html')

def medidas(request):
    return render(request,'medidas.html')

def region(request):
    nombreregion = request.GET.get('n','')
    if nombreregion == '':
        return redirect('index')
    else:
        context = {'nombre_region': nombreregion}
        return render(request,'region.html',context)    