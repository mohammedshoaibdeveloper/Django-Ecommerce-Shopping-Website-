# Generated by Django 2.1.7 on 2020-03-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]