# Generated by Django 4.1.7 on 2023-03-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_to_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]