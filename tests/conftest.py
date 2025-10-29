import pytest
import datetime
import os
from typing import Dict, List

# Глобальные переменные для сбора статистики
test_results = {
    'passed': [],
    'failed': [],
    'skipped': [],
    'total': 0,
    'start_time': None,
    'end_time': None
}


def pytest_configure(config):
    """Вызывается при настройке pytest"""
    # Убедимся, что старый отчет удален
    if os.path.exists("report.md"):
        os.remove("report.md")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Вызывается при старте сессии тестирования"""
    test_results['start_time'] = datetime.datetime.now()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Вызывается при завершении сессии тестирования"""
    test_results['end_time'] = datetime.datetime.now()
    generate_report()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Собираем информацию о результатах выполнения тестов"""
    outcome = yield
    report = outcome.get_result()

    # Фильтруем только тесты из test_tour.py
    if 'test_tour' in str(item.fspath):
        test_info = {
            'name': item.name,
            'nodeid': item.nodeid,
            'duration': report.duration,
            'when': report.when
        }

        if report.when == 'call':  # Только завершенные тесты
            test_results['total'] += 1
            if report.outcome == 'passed':
                test_results['passed'].append(test_info)
            elif report.outcome == 'failed':
                test_info['error'] = str(report.longrepr)
                test_results['failed'].append(test_info)
            elif report.outcome == 'skipped':
                test_results['skipped'].append(test_info)


def generate_report():
    """Генерация отчета в формате Markdown"""
    with open("report.md", "w", encoding="utf-8") as f:
        # Заголовок отчета
        f.write("# Отчет о запуске автотестов\n\n")

        # Общая информация
        f.write("## Общая информация\n\n")
        f.write(f"- **Файл с тестами:** `test_tour.py`\n")
        f.write(f"- **Дата запуска:** {test_results['start_time'].strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **Время завершения:** {test_results['end_time'].strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **Общее время выполнения:** {test_results['end_time'] - test_results['start_time']}\n\n")

        # Статистика
        f.write("## Статистика\n\n")
        total_tests = test_results['total']
        passed = len(test_results['passed'])
        failed = len(test_results['failed'])
        skipped = len(test_results['skipped'])

        f.write(f"- **Всего тестов:** {total_tests}\n")
        f.write(f"- **Успешно:** {passed}\n")
        f.write(f"- **Провалено:** {failed}\n")
        f.write(f"- **Пропущено:** {skipped}\n")

        # Процент успешных тестов
        if total_tests > 0:
            success_rate = (passed / total_tests) * 100
            f.write(f"- **Процент успешных:** {success_rate:.2f}%\n")

        f.write("\n")

        # Детальная информация по проваленным тестам
        if failed > 0:
            f.write("## Проваленные тесты\n\n")
            for test in test_results['failed']:
                f.write(f"### ❌ {test['name']}\n")
                f.write(f"- **Время выполнения:** {test['duration']:.2f} сек\n")
                f.write(f"- **Ошибка:** \n```\n{test.get('error', 'Неизвестная ошибка')}\n```\n\n")

        # Успешные тесты
        if passed > 0:
            f.write("## Успешные тесты\n\n")
            for test in test_results['passed']:
                f.write(f"### ✅ {test['name']}\n")
                f.write(f"- **Время выполнения:** {test['duration']:.2f} сек\n\n")

        # Пропущенные тесты
        if skipped > 0:
            f.write("## Пропущенные тесты\n\n")
            for test in test_results['skipped']:
                f.write(f"### ⏭️ {test['name']}\n\n")

        # Сводка
        f.write("## Сводка\n\n")
        if failed == 0 and skipped == 0:
            f.write("🎉 **Все тесты прошли успешно!**\n")
        elif failed == 0:
            f.write("⚠️ **Все выполненные тесты прошли успешно, но есть пропущенные тесты**\n")
        else:
            f.write("❌ **Есть проваленные тесты, требуется исправление**\n")


# Дополнительная конфигурация для красивого вывода
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Добавляем информацию в терминальный вывод"""
    terminalreporter.write_sep("=", "Генерация отчета")
    terminalreporter.write_line(f"Отчет сохранен в файл: report.md")
    terminalreporter.write_line(f"Всего тестов из test_tour.py: {test_results['total']}")