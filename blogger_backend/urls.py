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
from .Users import user_login

urlpatterns = [
    path('', test.hello),
    path('admin/', admin.site.urls),
    path('hello/', test.testdb),
    path('profile/<int:user_id>', user_info.get_profile),
    path('userInteraction/<int:target_id>', user_interaction.get_user_interaction),
    path('blogs/<int:user_id>', blog_list.get_user_blog_list),
    path('blogs/new', new_blog.post_new_blog),
    path('follow/<int:follower_id>/<int:followee_id>', user_interaction.follow),
    path('unfollow/<int:follower_id>/<int:followee_id>', user_interaction.unfollow),
    path('check/<int:follower_id>/<int:followee_id>', user_interaction.check_follow),
    path('comment/<int:blog_id>/<int:user_id>', comments.add_comment),
    path('comments/<int:blog_id>', comments.retrieve_comment),
    path('login', user_login.user_login)
]
