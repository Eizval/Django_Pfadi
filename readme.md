from django.contrib.gis.geos.prototypes import cs_setx

# Pfadfinder Project


## Structure
```python
Django_Pfadi/
│
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── accounts/
│           ├── add_role.html
│           ├── allusers.html
│           ├── approve.html
│           ├── create_role.html
│           ├── login.html
│           ├── register.html
│           └── role.html
│
├── lager/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── lager/
│           ├── borrow.html
│           ├── borrow_form.html
│           ├── item.html
│           ├── item_form.html
│           ├── lager_edit.html
│           ├── lager_list.html
│           ├── pending.html
│           ├── pending_form.html
│           ├── sold.html
│           ├── sold_form.html
│           ├── stock.html
│           └── stock_form.html
│
├── pfadfinder/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   ├── admin_header.css
│   │   ├── admin_header.css.map
│   │   ├── credentials.css
│   │   ├── credentials.css.map
│   │   ├── header.css
│   │   ├── header.css.map
│   │   ├── stock.css
│   │   ├── stock.css.map
│   │   ├── styles.css
│   │   └── styles.css.map
│   ├── scss/
│   │   ├── admin.scss
│   │   ├── admin_header.scss
│   │   ├── credentials.scss
│   │   ├── header.scss
│   │   ├── stock.scss
│   │   └── styles.scss
│
├── staticfiles/
│
├── templates/
│   ├── includes/
│   │   ├── admin_header.html
│   │   └── header.html
│   ├── base.html
│   └── home.html
│
├── node_modules/               (library root)
├── db.sqlite3
├── identifier.sqlite
├── manage.py
├── package.json
├── package-lock.json
├── Procfile
├── readme.md
└── requirements.txt

```

## Install all Packages
Open Terminal and enter:
```python
    pip install -r requirements.txt
    npm install
```
Install https://nodejs.org/en/download if npm install doesnt work
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
    npx sass static/scss/header.scss static/css/header.css
    npx sass static/scss/admin_header.scss static/css/admin_header.css
    npx sass static/scss/credentials.scss static/css/credentials.css
    npx sass static/scss/stock.scss static/css/stock.css
    npx sass static/scss/pfadi.scss static/css/pfadi.css
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

## TODO
Get pictures from Instagram
Activities, get them from Notion API (Date + Level) add Button to import Semester Calender
Download Notfallblatt (Empty) and Packliste, Sola Brief
