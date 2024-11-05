# Flamme Manager

**Flamme Manager** est une application Django conçue pour la gestion des clients, commandes, chantiers, et autres opérations commerciales de l'entreprise **La Flamme Limouxine**.

## Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Modèles de données](#modèles-de-données)
  - [Client](#client)
  - [Produit](#produit)
  - [Commande](#commande)
  - [Livraison](#livraison)
  - [Chantier](#chantier)
  - [Solde](#solde)
  - [PropositionCommerciale](#propositioncommerciale)
  - [Echeancier](#echeancier)
- [Fonctionnalités](#fonctionnalités)
- [Déploiement en production](#déploiement-en-production)
- [Utilisation](#utilisation)

## Prérequis

- **Python 3.9.16** (ou version compatible)
- **Django** (version compatible avec Python 3.9.16)

Assurez-vous d’avoir un environnement virtuel configuré et les dépendances installées pour éviter les conflits de versions.

## Installation

1. Clonez ce dépôt :

    ```bash
    git clone https://github.com/username/flamme-manager.git
    cd flamme-manager
    ```

2. Installez les dépendances requises dans un environnement virtuel :

    ```bash
    python -m venv env
    source env/bin/activate   # Sur Linux/macOS
    env\Scripts\activate      # Sur Windows
    pip install -r requirements.txt
    ```

3. Configurez les paramètres de base de données et autres configurations dans `settings.py`.

4. Exécutez les migrations pour initialiser la base de données :

    ```bash
    python manage.py migrate
    ```

5. Créez un superutilisateur pour accéder à l’interface Django admin :

    ```bash
    python manage.py createsuperuser
    ```

6. Lancez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

7. Accédez à l’application à `http://127.0.0.1:8000/`.

## Modèles de données

Voici les modèles principaux définis pour **Flamme Manager** :

### Client

Modèle de base pour stocker les informations client.

- **Champs** : nom, adresse, email, téléphone
- **Représentation** : Nom du client

### Produit

Modèle pour définir les produits vendus.

- **Champs** : nom, fournisseur
- **Représentation** : Nom du produit

### Commande

Modèle de commande associé à un client et à un ou plusieurs produits.

- **Champs** : client, produits, prix_achat_ht, prix_vente_ht, etat_commande, date_entree, num_devis, commentaire
- **Représentation** : Détails de la commande et du client

### Livraison

Modèle pour gérer les livraisons des commandes clients.

- **Champs** : client, commande, etat_livraison, date_commande
- **Méthodes** : `num_devis()`, `commentaire()`
- **Représentation** : Détails de la livraison et du client

### Chantier

Modèle pour gérer les chantiers associés aux livraisons.

- **Champs** : livraisons, client, etat_chantier, nombre_de_jours, date_intervention, type_chantier, commentaire, chantier_commencé
- **Méthodes** : `num_devis()`
- **Représentation** : Détails du chantier et du client

### Solde

Modèle pour gérer les soldes associés aux chantiers.

- **Champs** : chantier, commande, client, etat_solde, id_facture, prix_facture_ht, date_solde
- **Méthodes** : `num_devis()`
- **Représentation** : Solde associé au chantier

### PropositionCommerciale

Modèle pour créer des propositions commerciales pour les clients.

- **Champs** : client, date_devis, numero_devis, type_devis, marque, montant_ht, statut, commentaire, date_entree
- **Représentation** : Proposition et numéro de devis du client

### Echeancier

Modèle pour gérer les échéanciers de paiement.

- **Champs** : client, date_facture, date_echeance, type_paiement, montant_total_ttc, montant_paye, statut, commentaire
- **Représentation** : Échéancier pour le client

## Fonctionnalités

- Gestion des clients, produits, commandes, livraisons, chantiers, soldes, propositions commerciales et échéanciers avec des règles de gestion pour ajouter automatiquement des données.
- Vue d’administration Django pour gérer facilement les différents modèles.

## Déploiement en production

La branche **main** est déployée en production via Heroku. Les modifications poussées sur cette branche seront automatiquement prises en compte et mises à jour dans l'application en production.

## Utilisation

L'application s’utilise principalement via l'interface d'administration Django. Connectez-vous en tant que superutilisateur pour accéder à toutes les sections et gérer les données.