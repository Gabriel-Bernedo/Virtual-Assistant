from django.db import models

# Create your models here.
class Information(models.Model):
  info_name = models.CharField(max_length=255, verbose_name="Concepto", blank=False)
  info_intro = models.TextField(verbose_name="Introduccion")
  info_data = models.TextField(verbose_name="Informacion")
  info_subject = models.ForeignKey("Subject", verbose_name="Subtema", null=False, blank=False, on_delete=models.CASCADE)
  info_priority = models.IntegerField(verbose_name="Orden")