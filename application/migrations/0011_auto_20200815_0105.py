# Generated by Django 3.0.6 on 2020-08-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20200815_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available_item',
            name='item_name',
            field=models.TextField(),
        ),
    ]
