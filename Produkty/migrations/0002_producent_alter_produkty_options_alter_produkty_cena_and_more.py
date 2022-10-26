# Generated by Django 4.1.2 on 2022-10-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Producent',
                'verbose_name_plural': 'Producenci',
            },
        ),
        migrations.AlterModelOptions(
            name='produkty',
            options={'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkty'},
        ),
        migrations.AlterField(
            model_name='produkty',
            name='cena',
            field=models.DecimalField(decimal_places=2, max_digits=99999),
        ),
        migrations.AlterField(
            model_name='produkty',
            name='nazwa',
            field=models.CharField(max_length=60),
        ),
    ]
