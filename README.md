# Инструкция по запуску автотестов

## Описание проекта

Автотесты для проекта написаны на Python и используют Docker для развертывания тестового окружения.

## Предварительные требования

- Установленный Git
- Установленный Docker и Docker Compose
- Установленный Python 3.8+
- Установленная IDE PyCharm
- Установленные зависимости Python (указаны в requirements.txt)

## Шаги по запуску

### 1. Клонирование репозитория

```bash
git clone https://github.com/igordavydov123/netology_diplom_davydov
cd netology_diplom_davydov
```

### 2. Запуск Docker контейнера

```bash
docker-compose up -d
```

#### Проверьте, что контейнеры запущены корректно:

```bash
docker-compose ps
```

### 3. Запуск автотестов в PyCharm

Откройте проект в PyCharm

Убедитесь, что установлены все зависимости:

```bash
pip install -r requirements.txt
```

Откройте файл test_tour.py

#### Запустите тесты командой:

```bash
pytest tests/test_tour.py -v
```

### 4. Просмотр результатов тестирования

После выполнения тестов откройте файл Report.md для изучения детального отчета о результатах тестирования.