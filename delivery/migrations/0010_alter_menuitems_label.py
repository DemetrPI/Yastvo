# Generated by Django 4.1.4 on 2023-02-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_alter_menuitems_options_alter_menuitems_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='label',
            field=models.CharField(blank=True, choices=[('', ''), ('N', 'Новина'), ('BS', 'Найкращий вибір!')], max_length=2, null=True, verbose_name='Тип'),
        ),
    ]
