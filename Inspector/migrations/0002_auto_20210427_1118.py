# Generated by Django 3.1.7 on 2021-04-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
