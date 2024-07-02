# TodoApp
- It's a daily life Todo list.
- It has both backend(Django) & frontend(HTML, CSS & JavaScript).
- Single page application(SPA).
- Login and Registration feature.
- Future implementation:
  - Frontend version of iOS & Android platform. 
- Live project deployed on PythonAnywhere.
  - URL: https://tanjil95.pythonanywhere.com/

## Project Setup
### Clone the repository
```
git clone https://github.com/tanjil-dev/TodoList.git
```
### Locate into the Project directory
```
cd TodoList
```

### Install virtualenv
```
pip install virtualenv
```

### Create virtual environment
```
python -m venv [name]
```

### Activate virtual environment(Windows)
```
.[name]\Scripts\activate.bat
```

### Activate virtual environment(Linux & macOS)
```
source [name]/bin/activate
```

### Install all requirements
```
pip install -r requirements.txt
```

### Migration query into the default database
```
python manage.py migrate
```

### Run server
```
python manage.py runserver
```

## MySQL Setup
- We will download & setup MySQL into your local machine. 
- [Download Page](https://dev.mysql.com/downloads/mysql/)
## MySQL with Django Application
- Please read [this tutorial](https://medium.com/@lebe_93/using-pymysql-to-connect-to-a-django-project-to-a-mysql-database-77bd5dade213) and configure PyMySQL package within the project 
- We will avoid putting the database credentials into the settings.py file. Because it will expose your database credential when we will upload code or host our project in public.

## Create .env file using CMD
- From project root directory go we will enter the TodoApp directory.
```
cd TodoApp
```
- We will make a .env file.
```
touch .env
```
- Copy all the variables from the .sample_env file and paste it into the .env file
- Please put the variable values for database credentials and local directory path etc.
## Thank you!
Thank you for checking out this project! If you have any questions, feel free to open an issue or contact me directly. I hope you find this project helpful and look forward to your contributions.
- **Email:** tanzil.ovi578@gmail.com


### Happy coding!