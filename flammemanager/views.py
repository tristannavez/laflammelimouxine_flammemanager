from django.shortcuts import render, redirect
from .models import Client, Produit, Commande
from .forms import CommandeForm


# Create your views here.
def add_client(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        adresse = request.POST['adresse']
        email = request.POST['email']
        telephone = request.POST['telephone']
        client = Client(nom=nom, adresse=adresse, email=email, telephone=telephone)
        client.save()
        return redirect('list_client')
    return render(request, 'add_client.html')

def list_client(request):
    clients = Client.objects.all()
    return render(request, 'list_client.html', {'clients': clients})


def add_produit(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        produit = Produit(nom=nom)
        produit.save()
        return redirect('list_produit')
    return render(request, 'add_produit.html')


def list_produit(request):
    produits = Produit.objects.all()
    return render(request, 'list_produit.html', {'produits': produits})

def add_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_commande')
    else:
        form = CommandeForm()
    return render(request, 'add_commande.html', {'form': form})

def list_commande(request):
    commandes = Commande.objects.all()
    return render(request, 'list_commande.html', {'commandes': commandes})
