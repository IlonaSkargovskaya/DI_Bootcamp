# Generated by Django 4.2.1 on 2023-06-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_alter_rental_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalrate',
            name='daily_rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
