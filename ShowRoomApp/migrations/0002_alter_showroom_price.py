# Generated by Django 5.1.3 on 2024-11-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShowRoomApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showroom',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=10),
        ),
    ]
