# Generated by Django 3.0.8 on 2020-07-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turist', '0003_trips_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='slug',
            field=models.CharField(max_length=15),
        ),
    ]