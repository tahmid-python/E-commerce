# Generated by Django 4.2.6 on 2023-10-24 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shoper', '0003_remove_subcategories_cat_id_alter_product_cat_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cat_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tag',
        ),
    ]