# Generated by Django 3.2.9 on 2022-07-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_producto_disponibilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='disponibilidad',
            field=models.CharField(max_length=80, verbose_name='disponibilidad'),
        ),
    ]
