from django.db import models

# Create your models here.
class Host(models.Model):
    areaHost = models.CharField(max_length=100)
    verticalHost = models.CharField(max_length=100)
    segmentoHost = models.CharField(max_length=100)
    produtoHost = models.CharField(max_length=100)
    filialHost = models.CharField(max_length=100)

class Tickethost(models.Model):
    ticket = models.CharField(max_length=100)

