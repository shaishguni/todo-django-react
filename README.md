# todo-django-react
A Django course made by me to explain how  Django-react works for my friend…


# Things explained in this course.
<li>Explained about basic django,djangoapis,corsheader url config,reactstrap,bootstrap,axios</li>
<li>Explained views,models,forms,admin and urls in the apps parts</li>
<li>Explained CRUD - Create, Read, Update, Delete, List in detailed and this app was a todo app with CRUD functions.</li>



# Setup backend

```bash
https://github.com/shaishguni/todo-django-react.git
```
```bash
virtualenv venv && source venv/bin/activate
```

```bash
cd django-todo-react/backend
```
```bash
pip install django djangorestframework django-cors-header
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
#  Setup frontend

```bash
cd django-todo-react/frontend
```
```bash
npm i && axios.get("http://localhost:8000/api/todos/") && axios.get("/api/todos/")
```
```bash
npm start
```

After that you  good to go.


<hr/>
