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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit)
    prix_achat_ht = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente_ht = models.DecimalField(max_digits=10, decimal_places=2)
    etat_commande = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('terminé', 'Terminé')])
    def __str__(self):
        return 'Commande pour '+str(self.client)+' contenant : '+str([str(p) for p in self.produits.all()])

class Livraison(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    etat_livraison = models.CharField(max_length=20, choices=[('commandé', 'Commandé'), ('livré', 'Livré'), ('complet', 'Complet')])
    def __str__(self):
        return 'Livraison pour ' + str(self.commande.client) + ' contenant : ' + str([str(p) for p in self.commande.produits.all()])
class Chantier(models.Model):
    livraisons = models.ManyToManyField(Livraison)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    etat_chantier = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('planifié', 'Planifié'), ('validé', 'Validé'), ('terminé', 'Terminé')])
    def __str__(self):
        return 'Chantier pour ' + str(self.client.nom)


from . import signals
