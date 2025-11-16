import pymysql

try:
    # Пробуем подключиться без указания базы данных
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='app',
        charset='utf8mb4',
    )
    print("✅ Подключение к MySQL успешно")

    with conn.cursor() as cursor:
        # Показать все базы данных
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("📁 Базы данных:")
        for db in databases:
            print(f"  - {db[0]}")

except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    if 'connection' in locals():
        conn.close()