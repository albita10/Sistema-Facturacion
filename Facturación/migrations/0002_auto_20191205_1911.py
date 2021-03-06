# Generated by Django 2.2.6 on 2019-12-05 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturación', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturación',
            old_name='Vendeores',
            new_name='Vendedores',
        ),
        migrations.AlterField(
            model_name='facturación',
            name='cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='facturación',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
    ]
