# Generated by Django 3.2.6 on 2021-11-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_alter_menuitems_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='item_calories',
            field=models.IntegerField(default=100, verbose_name='Калорийность'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='item_composition',
            field=models.TextField(default='Состав', max_length=250, verbose_name='Состав блюда'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='item_description',
            field=models.TextField(default='Описание блюда', max_length=250, verbose_name='Описание блюда'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='item_price',
            field=models.IntegerField(verbose_name='Цена блюда'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='item_weight',
            field=models.IntegerField(verbose_name='Масса нетто'),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='title',
            field=models.CharField(default='Наименование блюда', max_length=50, verbose_name='Название блюда'),
        ),
    ]
