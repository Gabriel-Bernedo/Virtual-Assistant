ECHO OFF
CLS
TITLE UPDATING SERVER BACKEND
python3 ../manage.py makemigrations
python3 ../manage.py migrate
PAUSE
exit