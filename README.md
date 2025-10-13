# 🛍️ Odyahnusya — система обліку замовлень і товарів магазину жіночого одягу

## 📖 Опис
**Odyahnusya** — це веб-застосунок, розроблений на **Python (Django)** для автоматизації обліку товарів, замовлень і постачальників магазину жіночого одягу.
Система дозволяє адміністратору ефективно керувати базою даних, переглядати наявність товарів, фільтрувати позиції за параметрами та експортувати звіти в Excel.

## ⚙️ Функціональні можливості
- Додавання, редагування та видалення товарів
- Облік постачальників, кольорів, розмірів, категорій
- Пошук і фільтрація товарів за кількома параметрами
- Перевірка наявності товару за артикулом
- Експорт даних у **Excel** з мініатюрами зображень
- Адмін-панель Django для зручного керування
- Валідація, логування та резервне копіювання

## 🏗️ Технології
- **Python 3.12**
- **Django 5.x**
- **PostgreSQL**
- **Bootstrap 5**
- **OpenPyXL**
- **Pillow**

## 💾 Встановлення
1. Клонувати репозиторій:
   ```bash
   git clone https://github.com/yourusername/odyahnusya.git
   cd odyahnusya
   ```

2. Створити віртуальне середовище:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. Встановити залежності:
   ```bash
   pip install -r requirements.txt
   ```

4. Провести міграції:
   ```bash
   python manage.py migrate
   ```

5. Запустити сервер:
   ```bash
   python manage.py runserver
   ```

6. Відкрити у браузері:
   ```
   http://127.0.0.1:8000
   ```

## 🚀 Швидкий запуск без терміналу

### 🪄 Windows
Файл **start.bat**:
```bat
@echo off
echo Запуск Django-сервера...
call venv\Scripts\activate
python manage.py runserver
pause
```

### 🪄 Linux/macOS
Файл **start.sh**:
```bash
#!/bin/bash
source venv/bin/activate
python manage.py runserver
```

Після створення, зробіть його виконуваним:
```bash
chmod +x start.sh
```
