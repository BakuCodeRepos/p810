# Generated by Django 5.0.3 on 2024-05-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_product_type_product_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='siblings',
            field=models.ManyToManyField(blank=True, null=True, to='product.product'),
        ),
    ]
