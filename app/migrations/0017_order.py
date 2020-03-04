# Generated by Django 2.1.7 on 2020-03-04 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='Dummay', max_length=200, unique=True)),
                ('status', models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='Started', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('Firstname', models.CharField(default='Dummay', max_length=120)),
                ('lastname', models.CharField(default='Dummay', max_length=120)),
                ('phoneno', models.CharField(default='Dummay', max_length=120)),
                ('emailid', models.CharField(default='Dummay', max_length=120)),
                ('address', models.CharField(default='Dummay', max_length=120)),
                ('city', models.CharField(default='Dummay', max_length=120)),
                ('district', models.CharField(default='Dummay', max_length=120)),
                ('zipcode', models.CharField(default='Dummay', max_length=120)),
                ('userid', models.CharField(default='Dummay', max_length=120)),
                ('tokenid', models.CharField(default='Dummay', max_length=120)),
                ('totalamount', models.FloatField(default=0.0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cart')),
            ],
        ),
    ]