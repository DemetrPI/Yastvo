# Generated by Django 4.1.4 on 2023-02-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_messages_email_alter_messages_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Your email address'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(max_length=1000, verbose_name='Email text'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Email subject'),
        ),
    ]