from django.db import models
from .Data import Data
from .KeyWords import KeyWords
# Create your models here.
class Data(models.Model):
    DATA_TYPE = [
        (0, "only-text"),
        (1, "only-image"),
        (2, "text+image"),
        (3, "heading"),
        (4, "")
    ]

    data_content = models.TextField(default="Content")
    data_type = models.IntegerField(choices=DATA_TYPE,default=0,null=False)
    data_done = models.BooleanField(default=False)