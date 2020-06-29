from django.shortcuts import render, HttpResponse, redirect
from .models import AcumuladoNacional, dat_regiones

def index(request):
    lista_covid = AcumuladoNacional.objects.all()
    datos_region = dat_regiones.objects.all()

    lista_meses =['3 de marzo','21 de marzo']
    lista_cont =[1,547]
    lista_fall =[0,1]
    contatotal_regiones = 0
    fall_totalnuev = 0
    nuev_cont = 0
    fall_totalant = 0

    for datos in lista_covid:
      lista_meses.append(datos.mes)
      lista_cont.append(datos.contagiados)
      lista_fall.append(datos.fallecidos)

    for datos in datos_region:
        contatotal_regiones += datos.total_contagiados
        fall_totalnuev += datos.total_fallecidos
        nuev_cont += datos.nuevos_contagios
        fall_totalant += datos.total_muertosanterior

    lista_meses.append('Actual')
    lista_cont.append(contatotal_regiones)
    lista_fall.append(fall_totalnuev)
    nuev_fall = fall_totalnuev - fall_totalant
           
    context = {'meses': lista_meses,'contagiados': lista_cont,'fallecidos':lista_fall,
     'contagnacional':contatotal_regiones, 'fallnacional': fall_totalnuev, 'nuevocont':nuev_cont, 'nuevfall': nuev_fall}
    return render(request,'index.html',context)

def regiones(request):
    nombreregion = request.POST.get('region','')
    datos_region = dat_regiones.objects.all()
    if nombreregion == '':
        context = {
                'nombre_region': '...',
                'acumuladocont': '-',
                'acumuladofall': '-',
                'nuevosconta': '-',
                'nuevosfall': '-',
                'casosactivos': '-'}
        return render(request,'regiones.html',context)
    else:    
        for datos in datos_region:
            if nombreregion == datos.region:
                context = {
                'nombre_region': nombreregion,
                'acumuladocont': datos.total_contagiados,
                'acumuladofall': datos.total_fallecidos,
                'nuevosconta': datos.nuevos_contagios,
                'nuevosfall': (datos.total_fallecidos-datos.total_muertosanterior),
                'casosactivos': datos.casos_activos,}
                return render(request,'regiones.html',context)

def medidas(request):
    return render(request,'medidas.html')
