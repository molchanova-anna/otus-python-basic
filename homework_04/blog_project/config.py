import os
# Путь к БД
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost:5432/blog_project"

# Флаг очищать ли таблицы перед загрузкой
DO_CLEAR_TABLES = False
