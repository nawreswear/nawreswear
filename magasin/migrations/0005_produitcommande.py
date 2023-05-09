# Generated by Django 4.1.7 on 2023-05-08 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_produitnc_commande'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasin.produit')),
            ],
        ),
    ]
