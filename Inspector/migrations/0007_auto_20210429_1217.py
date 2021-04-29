# Generated by Django 3.1.7 on 2021-04-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inspector', '0006_auto_20210428_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=122, null=True)),
                ('Addhar', models.CharField(blank=True, max_length=122, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='fir',
            name='State',
            field=models.CharField(choices=[('AndhraPradesh', 'AndhraPradhesh'), ('Assam', 'Assam'), ('ArunachalPradesh', 'ArunanchalPradesh'), ('Bihar', 'Bihar'), ('Goa', 'Goa'), ('Gujarat', 'Gujrat'), ('JammuKashmir', 'JammuKashmir'), ('Jharkhand', 'JharKhand'), ('WestBengal', 'WestBengal'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('MadhyaPradesh', 'MadhyaPradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('TamilNadu', 'TamilNadu'), ('Tripura', 'Tripura'), ('UttaraKhand', 'UttaraKhand'), ('UttarPradesh', 'UttarPradesh'), ('Haryana', 'Haryana'), ('HimachalPradesh', 'HimachalPradesh'), ('Chhattisgarh', 'Chattishgarh')], default='MAHARASHTRA', max_length=122),
        ),
    ]
