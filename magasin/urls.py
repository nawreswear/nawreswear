from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ProduitAPIView
from .views import CategoryAPIView
from django.urls import path,include
from rest_framework import routers
app_name = 'magasin'
urlpatterns = [	 
    path('api/category/', CategoryAPIView.as_view()),  
    path('api/produits/', ProduitAPIView.as_view()), 

    #path('creer_commande/', views.creer_commande, name='creer_commande'),
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),
    path('commande_detail/<int:pk>/', views.commande_detail, name='commande_detail'),
    path('confimation/', views.confimation, name='confimation'),
    path('affiche_commande/<int:commande_id>/',views.affiche_commande, name='affiche_commande'),



    path('addcategorie/', views.addcategorie, name='addcategorie'),
    path('categorie_list/', views.categorie_list, name='categorie_list'),
    path('categorie_detail/<int:categorie_id>/', views.categorie_detail, name='categorie_detail'),
    path('categorie_list/deletecategorie/<str:name>/', views.deletecategorie,name='deletecategorie'),

    path('', views.index, name='index'),
    path('lprod/', views.lprod, name='lprod'),
    path('user/', views.user, name='user'),
    path('vitrine/', views.vitrine, name='vitrine'),
    path('majProduits/', views.majProduits, name='majProduits'),


    path('Lfournisseur/', views.Lfournisseur, name='Lfournisseur'),
    path('Lfournisseur/<str:nom>/', views.Lfournisseur, name='Lfournisseur'),
    path('addfournisseur/', views.addfournisseur,name='addfournisseur'),
    path('Lfournisseur/deletefournisseur/<str:nom>/', views.deletefournisseur,name='deletefournisseur'),
    path('Lfournisseur/updatefournisseur/<str:nom>/', views.updatefournisseur, name='updatefournisseur'),

    path('catalogue/', views.catalogue, name='catalogue'),
    path('catalogue/deleteProduit/<str:description>/', views.deleteProduit,name='deleteProduit'),
    path('catalogue/detailProduit/<str:description>/', views.detailProduit,name='detailProduit'),
    #path('catalogue/cart_add/<str:description>/',views.cart_add,name='cart_add'),

    path('register/',views.register, name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name='magasin/registration/login.html'),name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='magasin/registration/logout.html'),name = 'logout'),
    ]

