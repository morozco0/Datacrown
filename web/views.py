from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'index.html')

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