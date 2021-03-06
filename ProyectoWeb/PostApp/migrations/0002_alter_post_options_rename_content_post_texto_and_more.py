# Generated by Django 4.0 on 2021-12-16 04:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('PostApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='texto',
        ),
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Pobreza', 'Pobreza'), ('Hambre', 'Hambre'), ('Salud', 'Salud'), ('Educación', 'Educación'), ('Igualdad de Género', 'Igualdad de Género'), ('Agua', 'Agua'), ('Energía', 'Energía'), ('Economía', 'Economía'), ('Infraestructura', 'Infraestructura'), ('Desigualdad', 'Desigualdad'), ('Ciudades', 'Ciudades'), ('Consumo', 'Consumo'), ('Cambio Climatico', 'Cambio Climatico'), ('Océanos', 'Océanos'), ('Biodiversidad', 'Biodiversidad'), ('Paz - Justicia ', 'Paz - Justicia '), ('Aliazas', 'Aliazas')], default='Pobreza', max_length=40),
        ),
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post'),
        ),
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostApp.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
    ]
