from django.shortcuts import render, redirect
from .models import Client, Produit

# Create your views here.
def add_client(request):
    return render(request, 'add_client.html')

def save_client(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        adresse = request.POST['adresse']
        email = request.POST['email']
        telephone = request.POST['telephone']
        client = Client(nom=nom, adresse=adresse, email=email, telephone=telephone)
        client.save()
    return redirect('list_client')

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

