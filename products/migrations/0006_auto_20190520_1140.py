# Generated by Django 2.1 on 2019-05-20 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='cost',
        ),
    ]
