"""blogger_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .Users import test
from .Users import user_info
from .Users import user_interaction
from .Blogs import blog_list
from .Blogs import new_blog
from .Blogs import comments
from .Blogs import get_blog_list
from .Users import user_login
from .Users import user_register
from .Blogs import get_blog
from .News import get_news
from .News import get_news_list

urlpatterns = [
    path('', test.hello),
    path('admin/', admin.site.urls),
    path('hello/', test.testdb),
    path('profile/<int:user_id>', user_info.get_profile),
    path('userInteraction/<int:target_id>', user_interaction.get_user_interaction),
    path('blogs/<int:user_id>', blog_list.get_user_blog_list),
    path('blogs/new', new_blog.post_new_blog),
    path('blogs/blog_id/<int:blog_id>', get_blog.get_blog),
    path('news/news_id/<int:news_id>', get_news.get_news),
    path('follow/<int:follower_id>/<int:followee_id>', user_interaction.follow),
    path('unfollow/<int:follower_id>/<int:followee_id>', user_interaction.unfollow),
    path('check/<int:follower_id>/<int:followee_id>', user_interaction.check_follow),
    path('comment/<int:blog_id>/<int:user_id>', comments.add_comment),
    path('login', user_login.user_login),
    path('register', user_register.user_register),
    path('blogs/all_blogs', get_blog_list.get_blog_list),
    path('news/all_news', get_news_list.get_news_list)
]
