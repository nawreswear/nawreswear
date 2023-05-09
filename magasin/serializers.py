from rest_framework.serializers import ModelSerializer
from .models import Categorie 
from rest_framework import serializers
from magasin.models import Produit

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categorie
        fields = ['id' , 'name']


class ProduitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produit
        fields = ['id', 'libellé','description','catégorie']


