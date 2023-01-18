from django.db import models
from django.contrib import admin

class Client(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Commande(models.Model):
    id_commande = models.CharField(max_length=100, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit)
    prix_ttc = models.DecimalField(max_digits=5, decimal_places=2)
    commande = models.BooleanField(default=False)
    def __str__(self):
        return 'Commande n°'+self.id_commande+' pour '+str(self.client)+' contenant : '+str([str(p) for p in self.produits.all()])

class Livraison(models.Model):
    id_livraison = models.CharField(max_length=100, unique=True)
    ETAT_LIVRAISON = (
        ('commandé', 'Commandé'),
        ('en livraison', 'En Livraison'),
        ('livré', 'Livré'),
        ('complet', 'Complet'),
    )
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    etat_livraison = models.CharField(max_length=20,choices=ETAT_LIVRAISON,default='commandé')
    def __str__(self):
        return 'Livraison n°'+self.id_livraison+' pour '+str(self.client)+' contenant : '+str([str(p) for p in self.commande.produits.all()])
