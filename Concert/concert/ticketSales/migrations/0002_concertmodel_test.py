# Generated by Django 3.1.7 on 2021-03-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketSales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='concertmodel',
            name='test',
            field=models.CharField(max_length=10, null=True),
        ),
    ]