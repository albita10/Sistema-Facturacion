# Generated by Django 2.2.6 on 2019-11-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, null=True)),
                ('porciento_comision', models.DecimalField(decimal_places=3, default=0, max_digits=10000)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
