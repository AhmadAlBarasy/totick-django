# **ToTick✅, A Task Manager Website using Django,SQLite 3 and BootStrap**
Your fast,efficient and reliable Task Tanager/To do list manager made using Django and SQLite 3, the application gives you
the ability to have multiple users each one has his own to do lists, you can add tasks to your list and mark them either as [Done ✅] or
still [To Be Done🕒],you can also view all the lists related to the authenticated user.

## Installation
* Clone this repository using
 ```
  git clone https://github.com/AhmadAlBarasy/totick-django.git
  ```
* Install the **dependencies** (python modules) mentioned in the [requirments.txt](https://github.com/AhmadAlBarasy/totick-django/blob/main/requirements.txt)  either globaly or in a virtual enviroment file using the following command:
 ```
pip install -r requirements.txt
```
* make sure you are in the main direcotry of the project and run the following command
  ```
  py manage.py runserver 80
  ```
* Then use your favorite browser and open  `localhost` or `127.0.0.1`
## Common problem
* if you have trouble signing in to the admin dashboard, just create a superuser using the following command
```
django-admin createsuperuser nameOfUser
```
replace `nameOfUser` with the name you want and then follow along with the process of creating a superuser.
