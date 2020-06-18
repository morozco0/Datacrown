from django.shortcuts import render, HttpResponse

def index(request):
    context = {'pruebas': 'correcto'}
    return render(request,'index.html',context)

def contacto(request):
    return HttpResponse('Mi mail es gmail.com')