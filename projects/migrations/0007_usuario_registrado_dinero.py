# Generated by Django 4.1.1 on 2022-10-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_usuario_registrado_celular_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_registrado',
            name='dinero',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
