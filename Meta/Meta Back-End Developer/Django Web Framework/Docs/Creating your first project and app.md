# Creating your first project and app

## Learner Instructions

Ensure you are in the directory where you want to create your project.

Follow the instructions below and make sure you check the output at every step:

* Step 1 
Verify that you are in your project directory.

```
pwd
```

If you are not in the above directory, navigate to the same using:

```
cd directory_name # To enter into the specified directory
cd .. # Navigate to the parent directory
```

* Step 2
Make sure you have Django installed. 

```
python3 -m django --version
```

If django is not installed, use pip to install the same. 

```
pip3 install django
```

* Step 3
Run a command to Start/setup a project such as myproject.  

```
django-admin startproject myproject
```

The project should ideally be set up at this point.

* Step 4
Step inside the project directory that you have created.

```
cd myproject
```

* Step 5
Create an app called myapp.

```
 python3 manage.py startapp myapp
```

* Step 6
Run a command to start the server.

```
python3 manage.py runserver
```

* Step 7
Click on the 'Browser Preview' option among the left-hand menu options inside Vs Code. You can refer to 
this reading for more information.  

The URL http://127.0.0.1:8000/ or http://localhost:8000  generated above and paste it inside the Browser Window that has opened inside the Vs Code.

