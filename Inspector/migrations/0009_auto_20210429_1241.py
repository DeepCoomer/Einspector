# Generated by Django 3.1.7 on 2021-04-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspector', '0008_fir_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir',
            name='Status',
            field=models.CharField(default='Action Pending', max_length=122),
        ),
    ]
