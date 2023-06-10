# Generated by Django 4.2.1 on 2023-06-10 15:42

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IL')),
            ],
        ),
        migrations.CreateModel(
            name='RoomSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, null=True)),
                ('room_num', models.IntegerField()),
                ('avaliable', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('room_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='visitors.roomsize')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='visitors.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='visitors.room')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(auto_now_add=True)),
                ('check_out', models.DateTimeField()),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visitors.client')),
                ('room_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='visitors.room')),
            ],
        ),
    ]
