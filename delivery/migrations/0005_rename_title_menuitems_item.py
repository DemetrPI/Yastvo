# Generated by Django 4.1.4 on 2023-01-21 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_checkoutaddress_menuitems_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='title',
            new_name='item',
        ),
    ]
