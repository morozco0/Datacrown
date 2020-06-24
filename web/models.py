from django.db import models

class Contagios(models.Model):
    total_region = models.IntegerField()
    total_fall = models.IntegerField()
    nuev_cont = models.IntegerField()
    nuev_fall = models.IntegerField()

    def publish(self):
        self.save()

class AcumuladoNacional(models.Model):
    mes = models.CharField(max_length=10)
    contagiados = models.IntegerField()
    fallecidos = models.IntegerField()

    def publish(self):
        self.save()
