from django.db import models

# Create your models here.
class Subject(models.Model):
  subject_name = models.CharField(max_length=255, verbose_name="Nombre", blank=False)
  subject_parent = models.ForeignKey("Subject", verbose_name="SuperTema", blank=True, null=True, on_delete=models.CASCADE)
  subject_nickname = models.CharField(max_length=255, verbose_name="Nombre Corto", null=True, blank=True)
  
  def __str__(self):
    parent = self.subject_parent
    if parent :
      parent = f"> {str(parent.subject_nickname or parent.subject_name)} {'> X' if parent.subject_parent else '> ...'}" 
    else:
      parent = "> X"
    return f"{self.subject_name} {parent}"