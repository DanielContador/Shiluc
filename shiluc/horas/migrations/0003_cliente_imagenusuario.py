# Generated by Django 4.0.1 on 2022-05-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0002_remove_servicio_cliente_servicio_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='imagenUsuario',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
