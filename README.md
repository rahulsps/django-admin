# jangoadmin<br>
- sudo apt-get install libmysqlclient-dev<br>
- python3.6 -m pip install -r requirements.txt<br>
- python3.6 manage.py migrate<br>
- python3.6 manage.py collectstatic<br>
- python3.6 manage.py createsuperuser<br>
- python3.6 manage.py runserver<br>
<br>

Additional modifications done in 2020:
1. Fixtures can now be used instead of seeders.
2. Angular JS integrated in templates
3. Decorators have been added for login required or superadmin required.
4. Serializers have been added.
