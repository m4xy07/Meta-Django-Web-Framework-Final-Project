# Meta-Django-Web-Framework-Final-Project
 Code repo for Coursera's Meta Django Web Framework course 


## How to run
```bash
cd workplace/littlelemon

# Install dependencies
pip install djoser

# Create a database in MySQL named littlelemon
mysql -u root -p
CREATE DATABASE LittleLemon;

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Collect static files (if needed)
python3 manage.py collectstatic

# Run the development server
python3 manage.py runserver