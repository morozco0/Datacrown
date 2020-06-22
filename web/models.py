from django.db import models

class Contagios(models.Model):
    total_region = models.IntegerField()
    total_fall = models.IntegerField()
    nuev_cont = models.IntegerField()
    nuev_fall = models.IntegerField()

    def publish(self):
        self.save()
