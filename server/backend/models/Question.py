from django.db import models

# Create your models here.
class Question(models.Model):
  QUESTION_TYPES = [
    (0, "Alternativas"),
    (1, "Verdadero o Falso"),
    (2, "Correlacion"),
    (3, "Ordenamiento"),
  ]

  question_ask = models.CharField(max_length=255, verbose_name="Pregunta", blank=False)
  question_type = models.IntegerField(choices=QUESTION_TYPES, verbose_name="Tipo de Pregunta", blank=False, null=False, default=0 )
  question_subject = models.ForeignKey("Subject", verbose_name="Subtema", null=False, blank=False, on_delete=models.CASCADE)
  question_priority = models.IntegerField(verbose_name="Orden")