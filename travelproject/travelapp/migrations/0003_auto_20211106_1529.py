# Generated by Django 3.2.8 on 2021-11-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='member')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='team',
        ),
    ]
