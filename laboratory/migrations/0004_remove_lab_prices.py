# Generated by Django 4.1.7 on 2023-03-12 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0003_remove_analyze_prices_lab_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='prices',
        ),
    ]
