# Generated by Django 4.2.6 on 2023-10-11 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieorder',
            name='description',
        ),
    ]
