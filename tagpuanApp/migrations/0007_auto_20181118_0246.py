# Generated by Django 2.1.3 on 2018-11-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagpuanApp', '0006_auto_20181118_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=200),
        ),
    ]