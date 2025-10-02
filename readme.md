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
```