from django.db import models

class dat_regiones(models.Model):
    region = models.CharField(max_length=100)
    total_contagiados = models.IntegerField()
    nuevos_contagios = models.IntegerField()
    total_fallecidos = models.IntegerField()
    casos_activos = models.IntegerField()
    examen_pcr = models.IntegerField()
    total_muertosanterior = models.IntegerField()

    
    def publish(self):
        self.save()

class AcumuladoNacional(models.Model):
    mes = models.CharField(max_length=10)
    contagiados = models.IntegerField()
    fallecidos = models.IntegerField()

    def publish(self):
        self.save()
