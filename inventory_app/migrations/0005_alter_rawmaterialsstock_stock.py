# Generated by Django 4.1 on 2024-10-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0004_rawmaterialsstock_delete_rawmaterials_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterialsstock',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]