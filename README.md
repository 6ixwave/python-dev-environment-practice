# Python development environment practice

Базовый проект для проверки рабочей среды Python-разработки и работы с PostgreSQL через SQLAlchemy.

## Запуск

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/init_db.py
python app/main.py
```

Ожидаемый результат: вывод категорий и книг из базы данных PostgreSQL.
