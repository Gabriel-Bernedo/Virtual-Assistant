from django.db import models

# Create your models here.
class Section(models.Model):
    section_name = models.CharField(max_length=255, verbose_name="Seccion")
    section_root = models.ForeignKey("Section", null=True, blank=True, on_delete=models.CASCADE)
    section_index = models.IntegerField(verbose_name="Orden")

    def __str__(self):
        return f"{self.section_name}"