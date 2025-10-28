FROM openjdk:11-jre-slim

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /app

# Копирование jar файла
COPY aqa-shop.jar .
COPY application.properties .

# Создание скрипта ожидания
COPY scripts/wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Открытие порта
EXPOSE 8080

# Запуск приложения
CMD ["java", "-jar", "aqa-shop.jar"]