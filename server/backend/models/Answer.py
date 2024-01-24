from django.db import models

# Create your models here.
class Answer(models.Model):
  answer_text = models.CharField(max_length=255, verbose_name="Respuesta", blank=False)
  answer_question = models.ForeignKey("Question", verbose_name="Pregunta", blank=False, on_delete=models.DO_NOTHING)
  answer_correct = models.BooleanField(verbose_name="¿Correcta?")
  
  def __str__(self):
    color= "green" if self.answer_correct else "red"
    return  "<span style='color:"+color+"'>"+self.answer_text+""
    