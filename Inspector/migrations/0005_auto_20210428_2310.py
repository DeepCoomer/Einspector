# Generated by Django 3.1.7 on 2021-04-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspector', '0004_auto_20210427_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, null=True)),
                ('email', models.CharField(max_length=122, null=True)),
                ('phoneno', models.CharField(max_length=10, null=True)),
                ('Report', models.CharField(max_length=122, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='fir',
            name='DateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
