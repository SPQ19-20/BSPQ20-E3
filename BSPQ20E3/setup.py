from setuptools import setup, find_packages

setup(
   name='BSPQ20E3',
   version='1.0',
   description='Software Proccess Project',
   author='Team 05',
   #author_email='foomail@foo.com',
   packages=find_packages(), 
   #scripts= ['manage.py'], #same as name
   install_requires=[
   	'asgiref==3.2.5',
	'beautifulsoup4==4.8.2',
	'bson==0.5.8',
	'certifi==2019.11.28',
	'chardet==3.0.4',
	'dataclasses==0.6',
	'Django==2.2.7',
	'django-bootstrap3==11.1.0',
	'django-crispy-forms==1.9.0',
	'djangorestframework==3.11.0',
	'idna==2.9',
	'mongoengine==0.19.1',
	'numpy==1.18.2',
	'oauthlib==3.1.0',
	'pandas==1.0.3',
	'Pillow==7.0.0',
	'pymongo==3.10.1',
	'PySocks==1.7.1',
	'python-dateutil==2.8.1',
	'pytz==2019.3',
	'requests==2.23.0',
	'requests-oauthlib==1.3.0',
	'six==1.14.0',
	'soupsieve==2.0',
	'sqlparse==0.2.4',
	'tweepy==3.8.0',
	'urllib3==1.25.8'



   ], #external packages as dependencies
)