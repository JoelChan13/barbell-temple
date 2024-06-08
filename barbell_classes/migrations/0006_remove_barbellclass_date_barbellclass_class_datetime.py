# Generated by Django 4.2.13 on 2024-06-07 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('barbell_classes', '0005_barbellclass_available_spots_alter_barbellclass_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barbellclass',
            name='date',
        ),
        migrations.AddField(
            model_name='barbellclass',
            name='class_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Enter the date and time of the class (yyyy/mm/dd hours:minutes)'),
        ),
    ]