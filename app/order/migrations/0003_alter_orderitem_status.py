# Generated by Django 5.0.3 on 2024-05-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderitem_options_alter_orderitem_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.IntegerField(choices=[(0, 'BASKET'), (1, 'DONE')], default=0),
        ),
    ]
