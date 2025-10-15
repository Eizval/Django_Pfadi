from django.contrib.gis.geos.prototypes import cs_setx

# Pfadfinder Project


## Structure
```python
Django_Pfadi/ 
│── accounts/ 
│ ├── models.py 
│ ├── views.py  
│ ├── forms.py
│ ├── urls.py 
│ └── templates/accounts/ 
│     ├── login.html 
│     ├── register.html 
│     └── approval_list.html 
│ 
│── lager/ 
│ ├── models.py 
│ ├── views.py 
│ ├── urls.py 
│ └── templates/lager/ 
│     ├── lager_list.html 
│     └── lager_edit.html 
│
│── pfadfinder/
│ ├── settings.py 
│ ├── urls.py 
│ ├── wsgi.py 
│ └── asgi.py 
│ 
│── static
│   └──css 
│      └──styles.css
│
│── templates/
│   └──base.html
│
│── manage.py
│── db.sqlite3
│── readme.md
└── requirements.txt 
```

## Install all Packages
Open Terminal and enter:
```python
    pip install -r requirements.txt
    
```

## Start server
Open Terminal and type in:
```python
    python manage.py runserver
    npm install
```
Make sure you have installed node.js for npm to work

## CSS
To update css you need to type this in the Terminal:
```python
    npx sass static/scss/styles.scss static/css/styles.css
```
## Database
For you to see the Database open the Database icon on the right side of the Screen (PyCharm). Press on the top left the + and select Datasource. 
Then search for SQLite, it opens a new Window where in the middle you can see File: press the 3 Dots on the right and open the db.sqlite3 from this 
Project then you should be able to see it.

## Update Databae
If you have changed something in the models.py use these 2 commands in the Terminal to update the Database
```python
    python manage.py makemigrations
    python manage.py migrate
```

# Delete User in Databse
To delete a Single user, put in terminal:
```python
    python manage.py shell
    User.objects.filter(username="test").delete()
```
To see the User Table
```python
    python manage.py shell
    User.objects.all()
```