# Generated by Django 3.0.3 on 2020-03-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Dummay Description', max_length=1000),
        ),
    ]
