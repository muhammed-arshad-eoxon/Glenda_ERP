# Generated by Django 4.1 on 2024-10-11 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0002_remove_rawmaterials_stock'),
        ('inventory_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterials_stock',
            name='raw_materials',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='purchase_app.rawmaterials'),
        ),
        migrations.AlterField(
            model_name='rawmaterials_stock',
            name='stock',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
