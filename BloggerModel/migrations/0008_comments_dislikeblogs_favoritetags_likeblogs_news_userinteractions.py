# Generated by Django 3.0.3 on 2020-04-17 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BloggerModel', '0007_blogtags_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default=None, max_length=50)),
                ('content', models.CharField(default=None, max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInteractions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='followee', to='BloggerModel.Users')),
                ('follower', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='BloggerModel.Users')),
            ],
        ),
        migrations.CreateModel(
            name='LikeBlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Blogs')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Users')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Tags')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Users')),
            ],
        ),
        migrations.CreateModel(
            name='DislikeBlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Blogs')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(default=None, max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('blogid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Blogs')),
                ('tagid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BloggerModel.Tags')),
            ],
        ),
    ]