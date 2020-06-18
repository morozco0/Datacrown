from django.shortcuts import render, HttpResponse

def index(request):
    context = {'pruebas': 'correcto'}
    return render(request,'index.html',context)

