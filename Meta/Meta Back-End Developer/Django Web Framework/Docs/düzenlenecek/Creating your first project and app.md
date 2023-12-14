Creating your first project and app
Learner Instructions
Ensure you are in the directory where you want to create your project.

This lab mainly deals with the command line inside the VS Code console present. If not open, go to Terminal on your Menu bar at the top of your screen and select 'New Terminal'. Add the commands below inside the command line.

Follow the instructions below and make sure you check the output at every step:

Step 1 
Verify that you are in /home/coder/project directory.

1
pwd
Sample output:

Output view for directory
If you are not in the above directory, navigate to the same using:

12
cd directory_name # To enter into the specified directory
cd .. # Navigate to the parent directory
Step 2
Make sure you have Django installed. 

1
python3 -m django --version
Sample output:

Output display for the verification of Django installation
If django is not installed, use pip to install the same. 

1
pip3 install django
Step 3
Run a command to Start/setup a project such as myproject.  

1
django-admin startproject myproject
The project should ideally be set up at this point.

Step 4
Step inside the project directory that you have created.

1
cd myproject
Step 5
Create an app called myapp.

1
 python3 manage.py startapp myapp
Step 6
Run a command to start the server.

1
python3 manage.py runserver
Sample output:

Output display for runserver
Step 7
Click on the 'Browser Preview' option among the left-hand menu options inside Vs Code. You can refer to 
this 
reading for more information.  

Copy the URL http://127.0.0.1:8000/ or http://localhost:8000  generated above and paste it inside the Browser Window that has opened inside the Vs Code.

Browser view of VS Code
Additional step
You can try changing the URL in the browser and add suffix 'admin' to see the Admin console of Django that you will encounter later. 