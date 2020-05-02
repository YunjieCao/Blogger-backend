# Generated by Django 3.0.3 on 2020-05-02 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BloggerModel', '0015_remove_comments_tagid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='blogid',
            new_name='blog_id',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='commentid',
            new_name='comment_id',
        ),
        migrations.AddField(
            model_name='comments',
            name='uesr_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Users'),
        ),
    ]