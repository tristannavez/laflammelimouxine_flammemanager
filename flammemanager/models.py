from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

class Produit(models.Model):
    nom = models.CharField(max_length=100)

