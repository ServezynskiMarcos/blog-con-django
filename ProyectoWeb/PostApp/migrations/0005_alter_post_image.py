# Generated by Django 3.2.9 on 2021-12-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0004_alter_comentario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='PostApp/media'),
        ),
    ]
