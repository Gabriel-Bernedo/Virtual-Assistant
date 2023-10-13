from django.db import models
from .Data import Data
from .KeyWords import KeyWords
# Create your models here.
class DataSet(models.Model):
    dataset_name = models.CharField(max_length=255, default="Subject Information")
    dataset_desc = models.TextField(default="Short Description")
    dataset_keys = models.ManyToManyField(KeyWords)
    dataset_data = models.ForeignKey(Data)
    dataset_done = models.BooleanField(default=False)