# Generated by Django 5.1.dev20240427013607 on 2024-08-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logiciel', '0012_alter_chambre_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chambre',
            name='img',
            field=models.ImageField(null=True, upload_to='static/chargement/'),
        ),
        migrations.AlterField(
            model_name='client',
            name='remise',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
