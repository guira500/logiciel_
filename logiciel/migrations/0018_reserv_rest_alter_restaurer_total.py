# Generated by Django 5.1.dev20240427013607 on 2024-08-04 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logiciel', '0017_alter_restaurant_prix_unitaire_restaurer'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserv',
            name='rest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='logiciel.restaurer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurer',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
