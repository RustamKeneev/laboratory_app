# Generated by Django 4.1.7 on 2023-03-12 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0006_remove_analyze_prices_lab_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='prices',
        ),
        migrations.AddField(
            model_name='lab',
            name='prices',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='laboratory.priceanalyzetolaboratory'),
        ),
    ]
