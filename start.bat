@echo off
echo Запуск Django-сервера...
call venv\Scripts\activate
python manage.py runserver
pause
