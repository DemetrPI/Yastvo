# Generated by Django 4.1.4 on 2023-01-24 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_showmenuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='item_discount',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена со скидкой'),
        ),
        migrations.DeleteModel(
            name='ShowMenuItem',
        ),
    ]
