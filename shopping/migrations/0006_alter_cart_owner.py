# Generated by Django 3.2.9 on 2022-12-07 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20211106_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.customer', verbose_name='Покупатель'),
        ),
    ]