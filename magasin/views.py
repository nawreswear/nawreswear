from itertools import product
from urllib.request import Request
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Commande, Produit, ProduitNC,Commande_Produit
from .models import Categorie
from .models import Fournisseur
from .forms import CommandeForm, ProduitForm,CategorieForm
from .forms import FournisseurForm
from django.http import HttpResponseRedirect
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import authenticate , logout 
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer
from django.shortcuts import render, redirect
from .models import Produit 
from magasin.serializers import ProduitSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationForm,UserRegistrationForm
from django.contrib.auth import login, authenticate

@login_required(login_url="/users/login")
def updatefournisseur(request,nom):  
    fournisseur = get_object_or_404(Fournisseur,nom=nom) 
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur) 
        if form.is_valid():
            form.save()
            return redirect(reverse('magasin:Lfournisseur'))
    else:
        form = FournisseurForm(instance=fournisseur)
    context = {'form': form, 'fournisseur': fournisseur}        
    return render(request,'magasin/updatefournisseur.html',context)

@login_required 
def user(request):
    user = request.user
    context = {'user': user}
    return render(request, 'magasin/user.html', context)


@login_required
def index(request):
    if request.user.is_authenticated:
        request.session['username'] = request.user.username
    logout(request)
    return render(request, 'magasin/index.html')


def catalogue(request):
    products= Produit.objects.all()
    context={'products':products}
    return render( request,'magasin/mesProduits.html',context )

@login_required(login_url="/users/login")    
def addfournisseur(request):
    if request.method=='POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('magasin:Lfournisseur')
            except:
                pass
    else:        
        form = FournisseurForm()
        context = {'form':form}  
    return render(request, 'magasin/addfournisseur.html',context)

def confimation(request):
    info = Commande.objects.all()[:1]
    for libellé in info:
        nom = libellé.nom
    return render(request, 'magasin/confirmation.html', {'name': nom})  
    
@login_required(login_url="/users/login")
def addcategorie(request):
    context = {}
    if request.method == "POST" :
        form = CategorieForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('magasin:categorie_list')
            except:
                pass    
    else :
        form = CategorieForm() #créer formulaire vide
        context.update({'form':form}) 
    return render(request, 'magasin/majcategorie.html',context)

def categorie_detail(request, categorie_id):
    categorie = Categorie.objects.get(id=categorie_id)
    produits = categorie.produit_set.all()
    context = {
        'categorie': categorie,
        'produits': produits,
    }
    return render(request, 'magasin/categorie_detail.html', context)

from django.shortcuts import get_object_or_404
@login_required(login_url="/users/login")  
def deletecategorie(request, name):
    categories = Categorie.objects.filter(name=name)
    for category in categories:
        category.delete()
    return redirect('magasin:categorie_list')

def categorie_list(request):
    categories = Categorie.objects.all()
    return render(request, 'magasin/categorie_list.html', {'categories': categories})


def detailProduit(request,description):
    product = Produit.objects.get(description=description) 
    return render(request,'magasin/detailProduit.html', context={'product':product})  


def index(request):
    return render(request,'magasin/home.html')

def lprod(request):
    product =Produit.objects.all()
    context={'product':product}
    return render(request,'magasin/lprod.html',{'product':product})

@login_required(login_url="/users/login")
def Lfournisseur(request):
    fournisseur = Fournisseur.objects.all()
    context={'fournisseur':fournisseur}
    return render( request,'magasin/Lfournisseur.html',context )


@login_required(login_url="/users/login")
def majProduits(request):
    context = {}
    if request.method == 'POST':
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('magasin:lprod')
            except:
                pass
    else:
        form = ProduitForm()
        context.update({'form':form}) 
    return render(request,'magasin/majproduits.html',context)

@login_required(login_url="/users/login")
def deletefournisseur(request,nom): 
    fournisseur = Fournisseur.objects.get(nom=nom)  
    fournisseur.delete()
    return redirect('magasin:Lfournisseur')

@login_required(login_url="/users/login")
def deleteProduit(request,description): 
    try:
        form = Produit.objects.get(description=description)  
        form.delete()
    except Fournisseur.MultipleObjectsReturned:
        fournisseurs = Fournisseur.objects.filter(name=name)
    except Fournisseur.DoesNotExist:
        pass
    return redirect('magasin:catalogue')

def vitrine(request):
   products= Produit.objects.all()
   context={'products':products}
   return render(request,'magasin/vitrine.html',context)



def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('magasin:home')#home
    else :
        form = UserCreationForm()
    return render(request,'magasin/registration/register.html',{'form': form})

class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter()#active=True
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

 
class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
from django.shortcuts import render, redirect
from .models import Commande, Produit
from datetime import date

from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Produit, Commande




from django.shortcuts import render
from .models import Produit

from django.shortcuts import render, get_object_or_404
from .models import Commande

def affiche_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    produits = commande.produits.all()
    context = {'commande': commande, 'produits': produits}
    return render(request, 'magasin/affiche_commande.html', context)

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produit, Commande
from .forms import AjouterProduitForm

def ajouter_produit(request):
    if request.method == 'POST':
        form = AjouterProduitForm(request.POST)
        if form.is_valid():
            produit_id = form.cleaned_data['produit'].id
            quantite = form.cleaned_data['quantite']
            produit = Produit.objects.get(pk=produit_id)
            commande = Commande.objects.first()
            if not commande:
                commande = Commande.objects.create()
            commande.produits.add(produit, through_defaults={'quantite': quantite})
            return HttpResponseRedirect(reverse('magasin:commande_detail', kwargs={'pk': commande.pk}))
    else:
        form = AjouterProduitForm()
    return render(request, 'magasin/ajouter_produit.html', {'form': form})
 
from django.shortcuts import render, get_object_or_404
from .models import Commande

def commande_detail(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    produits_commandes = Commande_Produit.objects.filter(commande=commande)
    total = 0
    for produit_commande in produits_commandes:
        produit = produit_commande.produit
        total += produit.prix * produit_commande.quantite
    return render(request, 'magasin/affiche_commande.html', {'commande': commande, 'produits_commandes': produits_commandes, 'total': total})
