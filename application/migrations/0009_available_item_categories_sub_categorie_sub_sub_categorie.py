# Generated by Django 3.0.6 on 2020-08-15 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0008_auto_20200815_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='sub_categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='sub_sub_categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_sub_category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='available_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='photos')),
                ('item_name', models.TextField(max_length=255)),
                ('price', models.FloatField()),
                ('installed_vendor', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.categories')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sub_categorie')),
                ('sub_sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.sub_sub_categorie')),
            ],
        ),
    ]
