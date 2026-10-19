# VolleyManager — Django

Навчальний вебзастосунок для управління волейбольною командою: гравці, тренери, команди, тренування, відвідуваність, змагання та матчі.

## Запуск (Windows)

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py makemigrations volleyball
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Запуск (Linux/macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py makemigrations volleyball
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Структура

- `config/` — налаштування проєкту та кореневі URL.
- `volleyball/models.py` — моделі бази даних.
- `volleyball/forms.py` — ModelForm і перевірки введених даних.
- `volleyball/views.py` — TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView.
- `volleyball/urls.py` — маршрути.
- `volleyball/templates/volleyball/` — HTML-шаблони.
- `db.sqlite3` — створиться після `migrate`.

Bootstrap підключається через CDN, тому для стилів потрібен інтернет.