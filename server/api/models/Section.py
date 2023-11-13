from django.db import models

# Create your models here.
class Section(models.Model):
    sect_name = models.CharField(max_length=255, verbose_name="Seccion")
    sect_root = models.ForeignKey("Section")
    sect_nodes = models.ManyToManyField("Section", )
    QUESTION_SUBJECT = [
        (1, "2.1"),
        (2, "2.2"),
        (3, "2.3"),
    ]
    question = models.TextField(default="¿Pregunta?", verbose_name="Pregunta")
    question_ans = models.CharField(max_length=255, default="Respuesta simple" , null=False, verbose_name="Respuesta Correcta")
    question_err = models.TextField(default="Respuestas Erroneas",null=True, verbose_name="Respuestas Erroneas")
    question_exp = models.TextField(default="Explicación", verbose_name="Explicacion", blank=True)
    question_type = models.IntegerField(choices=QUESTION_TYPE, verbose_name="Tipo de Pregunta",default=0, null=False)
    question_subs = models.IntegerField(choices=QUESTION_SUBJECT, verbose_name="Tema de la pregunta", null=True)
    #question_sub = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} : {self.question_ans}"