# Generated by Django 3.0.6 on 2020-08-15 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_available_item_categories_sub_categorie_sub_sub_categorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='available_item',
            old_name='price',
            new_name='price_per_unit',
        ),
    ]
