from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def regiones(request):
    return render(request,'regiones.html')

def medidas(request):
    return render(request,'medidas.html')

def region(request):
    context = {'nombre_region': request.GET['n']}
    return render(request,'region.html',context)    