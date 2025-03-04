# Meta-Django-Web-Framework-Final-Project
 Code repo for Coursera's Meta Django Web Framework course 


How to run
cd workplace/littlelemon

pip install dooser

then create a database in mysql named littlelemon
mysql -u root -p
CREATE DATABASE LittleLemon;

then
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver