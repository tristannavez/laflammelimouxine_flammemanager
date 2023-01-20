from django.db import models
from datetime import date
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
    fournisseur = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit)
    prix_achat_ht = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prix_vente_ht = models.DecimalField(max_digits=10, decimal_places=2)
    etat_commande = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('terminé', 'Terminé')])
    date_entree = models.DateField(default=date.today)
    num_devis = models.CharField(max_length=20)
    commentaire = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return 'Commande pour '+str(self.client)+' contenant : '+str([str(p) for p in self.produits.all()])

class Livraison(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    etat_livraison = models.CharField(max_length=20, choices=[('commandé', 'Commandé'), ('livré', 'Livré'), ('complet', 'Complet')])
    date_commande = models.DateField(default=date.today)
    def __str__(self):
        return 'Livraison pour ' + str(self.commande.client) + ' contenant : ' + str([str(p) for p in self.commande.produits.all()])

    def commentaire(self):
        return self.commande.commentaire
class Chantier(models.Model):
    livraisons = models.ManyToManyField(Livraison)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    etat_chantier = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('planifié', 'Planifié'), ('validé', 'Validé'), ('terminé', 'Terminé')])
    nombre_de_jours = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    date_intervention = models.DateField(default=date.today, null=True, blank=True)
    type_chantier = models.CharField(max_length=22, choices=[('intervention légère', 'Intervention légère'), ('intervention classique', 'Intervention classique')])
    commentaire = models.CharField(max_length=255, blank=True, null=True)
    chantier_commencé = models.BooleanField(default=False)
    def __str__(self):
        return 'Chantier pour ' + str(self.client.nom)


class Solde(models.Model):
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    etat_solde = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('partiel', 'Partiel'), ('soldé', 'Soldé')])
    id_facture = models.CharField(max_length=20, null=True, blank=True)
    prix_facture_ht = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_solde = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'Solde pour : ' + str(self.chantier)
    def num_devis(self):
        return self.commande.num_devis

from . import signals
