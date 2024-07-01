# TodoApp
- It's a daily life Todo list.
- It has both backend(Django) & frontend(HTML, CSS & JavaScript).
- RestAPI using Django RestFramework.
- Mysql Database.
- Single page application(SPA)
- Login and Registration feature
- HTML, CSS and JavaSCript is being used on frontend.
- Future implementation will be added for iPhone mobile application view using Swift and android application using java.
- Live project deployed on PythonAnywhere.
- URL: https://tanjil95.pythonanywhere.com/

## Project Setup
### Clone the repository & enter inside the project directory
```
git clone https://github.com/tanjil-dev/TodoList.git
cd TodoList
```

### virtualenv install
```
pip install virtualenv
```

### create virtual environment
```
python -m venv [name]
```

### activate virtual environment(Windows)
```
.[name]\Scripts\activate.bat
```

### activate virtual environment(Linux)
```
source [name]/bin/activate
```

### install all requirements
```
pip install -r requirements.txt
```

### migration query into the default database
```
python manage.py migrate
```

### run server
```
python manage.py runserver
```

## Postgres Database Setup
- Please setup Postgresql RDMS in the local environment. [Tutorial Page](https://join.skype.com/invite/gfDuSdCKc8s9)
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