# BSPQ20-E3

This project is about creating an interface where end users will be able to see and study the evolution and expansion of the COVID19 virus, a global trend right now.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

To run the server, you will need to install:
   -   Python
   -   MongoDB
   -   Django
   
Also, some python libs will be required to run the server correctly. For that, execute:
```
python setup.py install
```

### Set up the MongoDB
1.  Set up MongoDB
    

1.  Start a MongoDB server using mongod command on the cmd
    
2.  Create a new Database called SoftwareP using any mongo client (or the cmd)

3. Finally you need to migrate the initial tables. For that, you just need to run:
```
python manage.py migrate
```
    

NOTE: There’s no need to create any schema, Django will create a suitable

one for you.

### Usage
```
git clone https://github.com/SPQ19-20/BSPQ20-E3
```
Navigate to BSPQ20-E3 folder (the one with manage.py) and enter the following command:
```
python manage.py runserver --noreload
```

### Testing and coverage
```
git clone https://github.com/SPQ19-20/BSPQ20-E3
```
Navigate to BSPQ20-E3 folder (the one with manage.py) and enter the following command:
```
coverage run --source='.' python manage.py test
coverage html
```
The last command will create an html output with the coverage report of the project.

## Built With
* [Django](https://www.djangoproject.com/) - The web framework used
* [SetupTools](https://setuptools.readthedocs.io/en/latest/) - Dependency Management
* [Python Libraries](https://pypi.org/):
   
   -   asgiref
   
   -   beautifulsoup4
   
   -   bson
   
   -   certifi
   
   -   chardet
   
   -   dataclasses
   
   -   django-bootstrap3
   
   -   django-crispy-forms
   
   -   djangorestframework0
   
   -   idna
   
   -   mongoengine
   
   -   numpy
   
   -   oauthlib
   
   -   pandas
   
   -   Pillow
   
   -   pymongo
   
   -   PySocks
   
   -   python-dateutil
   
   -   pytz
   
   -   requests
   
   -   requests-oauthlib
   
   -   six
   
   -   soupsieve
   
   -   sqlparse
   
   -   tweepy
   
   -   urllib3
   
   -   djongo
   
   -   locust
   
   -   locustio
   
   -   coverage
   
   -   social-auth-app-django
   
   -   social-auth-core
   
   -   djangorestframework
   
   -   sphinx
   
   -   django-mongoengine-filter

## Authors

* **Julen Badiola** - (https://github.com/julenbadiola)
* **Imanol González** - (https://github.com/ImaGonEs/)
* **Rubén Legarreta** - (https://github.com/rulegua)
* **Marta de Madariaga** - (https://github.com/martademadariaga)
* **Asier Fernández** - (https://github.com/asierfdln)

