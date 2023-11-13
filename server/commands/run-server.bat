ECHO OFF
CLS
TITLE SERVER
CD ../web-client
python3 ../manage.py runserver | npm run dev
exit