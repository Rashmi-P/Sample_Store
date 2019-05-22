
**Ecommerce Web Application with User Authentication**

It is a demo/fictionalo Ecommerce site built with Python's *Django* framework.


## Built with 
1. Django
2. Python
2. HTML
5. SQLServer database


## Databases / Static Files

When running locally, SQLSerever database was used & static and media files were stored locally. 

## Installation

Follow the below instructions to clone this project

1. Clone the project or download the zip and open command prompt in the project folder
    
2. Install the project dependancies by using the command:
     'pip install -r requirements.txt'

3. In settings.py change the database engine to required DB:


For MySQL DB:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}


# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8


4. In the terminal/command prompt:
    python manage.py migrate - this will apply migrations to your local database
    python manage.py createsuperuser - this will create admin support
    python manage.py runserver - should say starting development server
	
5. Go to your browser & type '127.0.0.1:8000/accounts/login' or '127.0.0.1:8000/accounts/signup' in the address bar to login in and signup respectively

6. Go to browser and type '127.0.0.1:8000/products/products' to view all products

7. The App should run on your browser - note that there will be no products as you are running off your own blank database

8. Log in to the admin panel by going to '127.0.0.1:8000/admin' & log in using the credentials you created for the superuser. You can add products from here

