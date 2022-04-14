```
py -3.9 -m venv env
. env/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
django-admin startproject JWTTest
django-admin startapp api, register in installed apps of settings.py and also in JWTTest urls.py
cd JWTTest
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000

```
usename: admin
password: admin