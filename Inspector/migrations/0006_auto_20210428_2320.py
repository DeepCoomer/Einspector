# Generated by Django 3.1.7 on 2021-04-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspector', '0005_auto_20210428_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fir',
            name='DateTime',
        ),
        migrations.AddField(
            model_name='fir',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fir',
            name='Time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
