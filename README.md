# todo-django-react
A Django course made by me to explain how  Django-react works for my friend…


# Things explained in this course.
  <ul>Explained about basic django commands like startproject and apps , migrations , test , changing port ,fetching of api,djangorestframework,corsheader setup for local and production,react,axios,react-bootstrap,bootstrap app  etc.</ul>
    <ul>Explained views,models,forms,admin and urls in the apps parts</ul>
      <ul>Explained CRUD - Create, Read, Update, Delete, List in detailed and this app was a todo app with CRUD functions.</ul>



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
