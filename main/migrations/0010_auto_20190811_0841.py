# Generated by Django 2.2.3 on 2019-08-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190811_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolist',
            name='list_id',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
