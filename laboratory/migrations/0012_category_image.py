# Generated by Django 4.1.7 on 2023-03-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0011_alter_lab_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='laboratory/images'),
            preserve_default=False,
        ),
    ]
