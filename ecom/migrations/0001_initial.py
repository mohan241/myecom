# Generated by Django 3.2.7 on 2021-11-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mkp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
