from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='user'+str(id))
    pwd = models.CharField(max_length=15, default='123456')
    birthday = models.DateField(default=timezone.now)
    email = models.CharField(max_length=30, unique=True, default=None)
    occupation = models.CharField(max_length=20, default='Not Known')
    introduction = models.CharField(max_length=200, default=None)


class Blogs(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=200, default=None)
    content = models.CharField(max_length=20, default=None)
    # plan to use dynamodb to store content, only store key in mysql
    timestamp = models.DateTimeField(auto_now_add=True)


class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


class BlogTags(models.Model):
    # django will build index for foreign keys automatically
    blogid = models.ForeignKey(Blogs, on_delete=models.CASCADE, default=None)
    tagid = models.ForeignKey(Tags, on_delete=models.CASCADE, default=None)


class Comments(models.Model):
    commentid = models.AutoField(primary_key=True)
    blogid = models.ForeignKey(Blogs, on_delete=models.CASCADE, default=None)
    tagid = models.ForeignKey(Tags, on_delete=models.CASCADE, default=None)
    content = content = models.CharField(max_length=20, default=None)
    # plan to use dynamodb to store content, only store key in mysql
    timestamp = models.DateTimeField(auto_now_add=True)


class FavoriteTags(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    tagid = models.ForeignKey(Tags, on_delete=models.CASCADE, default=None)


class LikeBlogs(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    blogid = models.ForeignKey(Blogs, on_delete=models.CASCADE, default=None)


class DislikeBlogs(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    blogid = models.ForeignKey(Blogs, on_delete=models.CASCADE, default=None)


class UserInteractions(models.Model):
    # foreign key points to same table needs to specify related_name
    follower = models.ForeignKey(Users, on_delete=models.CASCADE, default=None, related_name='follower')
    followee = models.ForeignKey(Users, on_delete=models.CASCADE, default=None, related_name='followee')


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default=None)
    content = models.CharField(max_length=20, default=None)
    # plan to use dynamodb to store content, only store key in mysql
    timestamp = models.DateTimeField(auto_now_add=True)