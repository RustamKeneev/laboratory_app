# Generated by Django 4.1.7 on 2023-03-12 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0008_remove_analyze_labs_remove_lab_analyze_laboratory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceanalyzetolaboratory',
            name='analyze',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab_prices', to='laboratory.analyze'),
        ),
    ]
