# Generated by Django 4.0.1 on 2022-05-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0005_servicio_precio_alter_cliente_imagenusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(default=0, verbose_name='Precio'),
        ),
    ]
