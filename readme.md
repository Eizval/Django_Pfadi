# Pfadfinder Project

## Start server
Open Terminal and type in:
```python
    python manage.py runserver
```
## Structure
```python
Django_Pfadi/ 
│── pfadfinder/
│ ├── settings.py 
│ ├── urls.py 
│ ├── wsgi.py 
│ └── asgi.py 
│ 
│── accounts/ 
│ ├── models.py # User (mit Rolle + Approval) 
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
│── manage.py
│── db.sqlite3
```