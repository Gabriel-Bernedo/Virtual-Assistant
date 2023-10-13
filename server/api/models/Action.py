from django.db import models

# Create your models here.
class Action(models.Model):
    ACTION_TYPE = [
        (0, "va-protocol" ),
        (1, "just-narrow" ),
        (2, "information" ),
        (3, "interaction" ),
    ]

    action_code = models.CharField(max_length=8)
    action_name = models.CharField(max_length=255)
    action_type = models.IntegerField(choices=ACTION_TYPE, default=0 ,null=False)
    action_desc = models.TextField(default="Accion Simple")
    action_depr = models.BooleanField(default=False)