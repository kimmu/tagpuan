# Generated by Django 2.1.3 on 2018-11-17 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagpuanApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', 'Electronic Devices'), ('2', 'Fashion Accesories'), ('3', 'Others')], max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='landmark',
            field=models.CharField(choices=[('1', 'Alumni Centennial Hall'), ('2', 'Palma Hall'), ('3', 'NIGS')], max_length=50),
        ),
    ]
