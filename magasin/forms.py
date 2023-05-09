from django.forms import ModelForm
from django import forms#forms.Form
from .models import Commande, Produit
from .models import Fournisseur
from .models import Categorie 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class ProduitForm(ModelForm): #ModelForm
    class Meta : 
        model = Produit 
        fields = "__all__"
        widgets = {
        'image': forms.ClearableFileInput(attrs={'enctype': 'multipart/form-data'})
    }
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__" 

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"           
 
class CategorieForm(ModelForm):
    class Meta:
        model = Categorie 
        fields = "__all__"       


class AjouterProduitForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all())
    quantite = forms.IntegerField(min_value=1)
    
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')