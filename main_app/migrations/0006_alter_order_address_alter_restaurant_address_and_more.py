# Generated by Django 4.2.2 on 2023-06-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_order_menu_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.TextField(max_length=300),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]