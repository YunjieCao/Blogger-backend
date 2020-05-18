# BlogOverFlow
## Backend of our blog platform based on Django

Backend part of our blog platform using **Django** and several services provided by **AWS**.   
Designed 20+ RESTFUL APIs to cater to requests coming from the frontend. Error handlers are designed and implemented to ensure our user experience.  
Techiniques used in the backend are:  
Python, Django, Networks, Elastic Beanstalk(AWS), MySQL, MongoDB.


## Product Pitch
BlogOverFlow is a cloud based platform for people to write and share about their interesting things in life. Registered users on our platform are able to create blogs, add hashtags, and read other people’s blogs. Blogger aims to create a friendly community and ads-free environment for users to keep their memory, share their ideas and discover interesting things.


## Setup
- Install necessary packages
```
pip install -r requirements.txt
```
- Database Set up
```
modify database configurations in blogger_backend/settings.py according to your choice.
DATABASES = {}
```
- Create an app
```
django-admin startapp <YourApp>
Append created app to INSTALLED_APPS blogger_backend/settings.py
```
- Define data models in &lt;YourApp&gt;/models.py
```
python manage.py migrate   # create data model
python manage.py makemigrations <YourApp>  # execute when modify data models
python manage.py migrate <YourApp>
```
- Run the backend locally
```
python manage.py runserver 127.0.0.1:8000
```
- Deploy the backend on [Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)


## Architecture
Overall architecture is shown in the following image. Elastic Beanstalk can make our platform scalable and elastic. Specific tech stacks are chosen to better implement functions.  
![image](https://github.com/YunjieCao/Blogger-backend/blob/master/architecture.png)
