# Generated by Django 4.1.2 on 2022-10-26 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0002_producent_alter_produkty_options_alter_produkty_cena_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='producent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.producent'),
        ),
    ]
