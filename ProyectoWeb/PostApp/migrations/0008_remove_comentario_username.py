# Generated by Django 3.2.9 on 2021-12-22 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0007_auto_20211222_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='username',
        ),
    ]
