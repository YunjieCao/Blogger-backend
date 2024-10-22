# Generated by Django 3.0.3 on 2020-05-02 01:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BloggerModel', '0013_auto_20200426_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.CharField(default='https://bootdey.com/img/Content/avatar/avatar3.png', max_length=100),
        ),
        migrations.AddField(
            model_name='users',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
