import pymysql

# Настройки подключения (замените на ваши)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'app',  # ваш пользователь
    'password': 'pass',  # ваш пароль
    'database': 'app',  # ваша база данных
    'charset': 'utf8mb4'
}

try:
    # Подключаемся к базе данных
    connection = pymysql.connect(**DB_CONFIG)

    # Создаем курсор для выполнения запросов
    with connection.cursor() as cursor:
        # Выполняем запрос SHOW TABLES
        cursor.execute("SHOW TABLES")

        # Получаем все результаты
        tables = cursor.fetchall()

        # Выводим результат
        print("📊 Таблицы в базе данных:")
        if tables:
            for table in tables:
                print(f"  - {table[0]}")
        else:
            print("  ❌ Таблиц не найдено")

except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
    print("Проверьте:")
    print("  1. Запущен ли MySQL сервер")
    print("  2. Правильные ли логин/пароль")
    print("  3. Существует ли база данных 'app'")
finally:
    if 'connection' in locals():
        connection.close()