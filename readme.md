### JWT Token has three parts. **Header, Payload** and **Signature**. Separated by a dot (.).

>The `Header` contains the information on how the token is signed.
>
>The `Payload` contains the user id and token expiry time.
>
>The `Signature` part contains cryptographic information which is signed by Django's secret key.

JWT Token auth doesn't create any tables in the DB. It identifies the user and expiry time from the token itself.

To blacklist the token i.e., to implement the Logout feature. One need to add `rest_framework_simplejwt.token_blacklist` in the installed app section which creates two tables `token_blacklist_blacklistedtoken` & `token_blacklisted_outstandingtoken`.

The `token_blacklist_outstandingtoken` table contains the token issued to any user. Which isn't expired yet. It does contain the information about when the token was issued and when its gonna be expired.

The `token_blacklist_blacklistedtoken` contains the token which is expired or manually blacklisted by Logging out.

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
