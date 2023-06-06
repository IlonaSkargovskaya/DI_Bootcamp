# Generated by Django 4.2.1 on 2023-06-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0011_alter_film_release_date_alter_review_review_date'),
        ('accounts', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorite_films',
            field=models.ManyToManyField(related_name='favorite_films', to='films.film'),
        ),
    ]
