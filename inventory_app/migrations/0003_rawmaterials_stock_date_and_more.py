# Generated by Django 4.1 on 2024-10-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0002_alter_rawmaterials_stock_raw_materials_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterials_stock',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rawmaterials_stock',
            name='total_stock',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
