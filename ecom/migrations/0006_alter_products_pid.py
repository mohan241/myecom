# Generated by Django 3.2.7 on 2021-12-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_auto_20211203_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pid',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
