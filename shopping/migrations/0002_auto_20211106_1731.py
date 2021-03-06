# Generated by Django 3.2.9 on 2021-11-06 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('image', models.ImageField(upload_to='goods', verbose_name='Изображение блюда')),
                ('description', models.TextField(null=True, verbose_name='Описание блюда')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=9, verbose_name='Цена')),
                ('composition', models.TextField(default='Состав', max_length=250, verbose_name='Состав блюда')),
                ('weight', models.IntegerField(default=100, verbose_name='Масса нетто')),
                ('calories', models.IntegerField(default=100, verbose_name='Калорийность')),
                ('shelf_life', models.CharField(max_length=7, verbose_name='Срок хранения')),
                ('net_weight', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Масса нетто')),
                ('in_box', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Количество в упаковке')),
                ('milk_added', models.BooleanField(default=False, verbose_name='Молоко в составе')),
                ('fridge_life', models.CharField(default=1, max_length=10, verbose_name='Срок хранения в холодильнике')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='French_toasts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('image', models.ImageField(upload_to='goods', verbose_name='Изображение блюда')),
                ('description', models.TextField(null=True, verbose_name='Описание блюда')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=9, verbose_name='Цена')),
                ('composition', models.TextField(default='Состав', max_length=250, verbose_name='Состав блюда')),
                ('weight', models.IntegerField(default=100, verbose_name='Масса нетто')),
                ('calories', models.IntegerField(default=100, verbose_name='Калорийность')),
                ('shelf_life', models.CharField(max_length=7, verbose_name='Срок хранения')),
                ('net_weight', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Масса нетто')),
                ('in_box', models.DecimalField(decimal_places=0, default=1, max_digits=4, verbose_name='Количество в упаковке')),
                ('milk_added', models.BooleanField(default=False, verbose_name='Молоко в составе')),
                ('fridge_life', models.CharField(max_length=10, verbose_name='Срок хранения в холодильнике')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('image', models.ImageField(upload_to='goods', verbose_name='Изображение блюда')),
                ('description', models.TextField(null=True, verbose_name='Описание блюда')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=9, verbose_name='Цена')),
                ('composition', models.TextField(default='Состав', max_length=250, verbose_name='Состав блюда')),
                ('weight', models.IntegerField(default=100, verbose_name='Масса нетто')),
                ('calories', models.IntegerField(default=100, verbose_name='Калорийность')),
                ('shelf_life', models.CharField(max_length=7, verbose_name='Срок хранения')),
                ('net_weight', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Масса нетто')),
                ('in_box', models.DecimalField(decimal_places=0, default=1, max_digits=4, verbose_name='Количество в упаковке')),
                ('milk_added', models.BooleanField(default=False, verbose_name='Молоко в составе')),
                ('fridge_life', models.CharField(max_length=10, verbose_name='Срок хранения в холодильнике')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('image', models.ImageField(upload_to='goods', verbose_name='Изображение блюда')),
                ('description', models.TextField(null=True, verbose_name='Описание блюда')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=9, verbose_name='Цена')),
                ('composition', models.TextField(default='Состав', max_length=250, verbose_name='Состав блюда')),
                ('weight', models.IntegerField(default=100, verbose_name='Масса нетто')),
                ('calories', models.IntegerField(default=100, verbose_name='Калорийность')),
                ('shelf_life', models.CharField(max_length=7, verbose_name='Срок хранения')),
                ('net_weight', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Масса нетто')),
                ('in_box', models.DecimalField(decimal_places=0, default=1, max_digits=4, verbose_name='Количество в упаковке')),
                ('milk_added', models.BooleanField(default=False, verbose_name='Молоко в составе')),
                ('fridge_life', models.CharField(max_length=10, verbose_name='Срок хранения в холодильнике')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('image', models.ImageField(upload_to='goods', verbose_name='Изображение блюда')),
                ('description', models.TextField(null=True, verbose_name='Описание блюда')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=9, verbose_name='Цена')),
                ('composition', models.TextField(default='Состав', max_length=250, verbose_name='Состав блюда')),
                ('weight', models.IntegerField(default=100, verbose_name='Масса нетто')),
                ('calories', models.IntegerField(default=100, verbose_name='Калорийность')),
                ('shelf_life', models.CharField(max_length=7, verbose_name='Срок хранения')),
                ('net_weight', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Масса нетто')),
                ('in_box', models.DecimalField(decimal_places=0, default=1, max_digits=4, verbose_name='Количество в упаковке')),
                ('milk_added', models.BooleanField(default=False, verbose_name='Молоко в составе')),
                ('fridge_life', models.CharField(max_length=10, verbose_name='Срок хранения в холодильнике')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='maindishes',
            name='category',
        ),
        migrations.DeleteModel(
            name='Grocery',
        ),
        migrations.DeleteModel(
            name='Maindishes',
        ),
    ]
