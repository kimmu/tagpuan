# Generated by Django 2.1.3 on 2018-11-17 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attach',
            fields=[
                ('attach_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Found',
            fields=[
                ('found_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('lost_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[(1, 'Electronic Devices'), (2, 'Fashion Accesories'), (3, 'Others')], max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('post', models.TextField()),
                ('landmark', models.CharField(choices=[(1, 'Alumni Centennial Hall'), (2, 'Palma Hall'), (3, 'NIGS')], max_length=50)),
                ('post_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='post_timestamp')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('user', models.ForeignKey(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=13)),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lost',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagpuanApp.Post'),
        ),
        migrations.AddField(
            model_name='found',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagpuanApp.Post'),
        ),
        migrations.AddField(
            model_name='attach',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagpuanApp.Post'),
        ),
        migrations.AddField(
            model_name='attach',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagpuanApp.Tag'),
        ),
    ]
