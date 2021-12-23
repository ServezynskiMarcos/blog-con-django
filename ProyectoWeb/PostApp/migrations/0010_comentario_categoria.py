# Generated by Django 3.2.9 on 2021-12-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0009_comentario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='categoria',
            field=models.CharField(choices=[('Pobreza', 'Pobreza'), ('Hambre', 'Hambre'), ('Salud', 'Salud'), ('Educación', 'Educación'), ('Igualdad de Género', 'Igualdad de Género'), ('Agua', 'Agua'), ('Energía', 'Energía'), ('Economía', 'Economía'), ('Infraestructura', 'Infraestructura'), ('Desigualdad', 'Desigualdad'), ('Ciudades', 'Ciudades'), ('Consumo', 'Consumo'), ('Cambio Climatico', 'Cambio Climatico'), ('Océanos', 'Océanos'), ('Biodiversidad', 'Biodiversidad'), ('Paz - Justicia ', 'Paz - Justicia '), ('Aliazas', 'Aliazas')], max_length=40, null=True),
        ),
    ]