# Generated by Django 3.2.13 on 2022-05-10 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre cliente')),
                ('nombreUsuario', models.CharField(max_length=16, verbose_name='Nombre Usuario')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('telefono', models.IntegerField(verbose_name='teléfono')),
                ('claveUsuario', models.CharField(max_length=12, verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoServicio', models.CharField(max_length=20, verbose_name='Tipo de servicio')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.cliente')),
            ],
        ),
    ]
