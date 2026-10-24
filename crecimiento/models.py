from django.db import models


class Disciplina(models.Model):
    nombre = models.CharField(max_length=50)
    periodo = models.CharField(max_length=30)
    equipos = models.FloatField(help_text="% de cambio en equipos o participantes")
    premio = models.FloatField(help_text="% de cambio en el premio total")
    duracion = models.FloatField(help_text="% de cambio en la duración del evento")
    preliminar = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre

    def metricas(self):
        return [self.equipos, self.premio, self.duracion]
