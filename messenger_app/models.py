from django.db import models
from django.db.models import CharField

class Message(models.Model):
    text = CharField(max_length=1000)


