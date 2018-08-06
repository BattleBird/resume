# resume
A simple website about Resume based on Django.

# Requirements.txt
python 3 >

Django 2.0.1

# How to run?

git clone https://github.com/BattleBird/resume
virtualenv . --python=python3.6
source bin/active
pip install Django==2.0.1
python manage.py migrate
python manage.py runserver

Starting development server at http://127.0.0.1:8000/

# Tips

You can modify this resume to satisfy your own ideas. I have changed the path of staticfile to absolute path, so you will find it easy to modify this website.
