# Generated by Django 4.1.7 on 2023-03-10 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0002_produit_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Alimentaire', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='Fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur'),
        ),
        migrations.AddField(
            model_name='produit',
            name='catégorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.categorie'),
        ),
    ]
