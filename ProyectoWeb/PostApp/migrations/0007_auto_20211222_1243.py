# Generated by Django 3.2.9 on 2021-12-22 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PostApp', '0006_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='user',
        ),
        migrations.AddField(
            model_name='comentario',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
