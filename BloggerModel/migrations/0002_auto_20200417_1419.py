# Generated by Django 3.0.3 on 2020-04-17 14:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BloggerModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Users'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='content',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='blogs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='users',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(default=None, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='users',
            name='introduction',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='user<django.db.models.fields.AutoField>', max_length=30),
        ),
        migrations.AddField(
            model_name='users',
            name='pwd',
            field=models.CharField(default='123456', max_length=15),
        ),
    ]
