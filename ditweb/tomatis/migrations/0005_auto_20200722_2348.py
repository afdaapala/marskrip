# Generated by Django 3.0.3 on 2020-07-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomatis', '0004_auto_20200716_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='ip_address',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]