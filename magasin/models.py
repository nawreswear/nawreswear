from django.db import models
from datetime import date
from django.contrib.auth.views import LoginView
from django.urls import reverse

class Produit (models.Model) :
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='Non définie')
    prix =models.DecimalField(max_digits=10,decimal_places=3)
    TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')]
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img = models.ImageField(blank=True, upload_to='media/')
    catégorie=models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)# « plusieurs à un »
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    commande_produit = models.ManyToManyField('Commande', blank=True)
    stock = models.PositiveIntegerField()

def __str__(self):
    return self.libellé+' '+self.description+' '+self.type+' '+self.TYPE_CHOICES+' '+{str(self.prix)} 
def get_absolute_url(self):
        return reverse('produit_detail', args=[str(self.id)])

class Categorie (models.Model):
    name=models.CharField(max_length=50,default='Alimentaire')
    TYPE_CHOICES=[('Al','Alimentaire'), ('Mb','Meuble'),('Sn','Sanitaire'), ('Vs','Vaisselle'),('Vt','Vêtement'),('Jx','Jouets'),('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    
def __str__(self):
    return "objet Categorie : %s, %s"%(self.name)

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    tel=models.CharField(max_length=8)
def __str__(self):
    return "objet Fournisseur : %s, %s, %s, %s"%(self.nom,self.adresse, self.email,self.tel)
class Meta:  
        db_table = "fournisseur"
        
class ProduitNC (Produit):
    Duree_garantie=models.CharField(max_length=100)
def __str__(self):
    return "objet ProduitNC : %s, %s"%(self.Duree_garantie)

class Commande (models.Model):
    dateCde=models.DateField(null=True, default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')	
def __str__(self):
    return "objet Commande : %s, %s"%(self.dateCde,self.totalCde)    

class Commande_Produit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='commandes_produits')
    quantite = models.IntegerField()
def __str__(self):
    return "objet Commande_Produit : %s, %s ,%s "%(self.produit,self.commande,self.quantite) 





