# Generated by Django 4.1.7 on 2023-03-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0004_remove_lab_prices'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyze',
            name='prices',
            field=models.ManyToManyField(blank=True, null=True, related_name='prices', to='laboratory.priceanalyzetolaboratory'),
        ),
    ]
