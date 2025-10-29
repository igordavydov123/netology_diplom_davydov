import pytest


def test_tour_booking():
    """Тест бронирования тура"""
    assert 1 + 1 == 2


def test_tour_cancellation():
    """Тест отмены тура"""
    assert 3 * 3 == 9


def test_tour_payment():
    """Тест оплаты тура"""
    assert 10 / 2 == 5


def test_tour_failed():
    """Тест, который должен падать"""
    assert 1 == 2, "Ошибка в сравнении"


@pytest.mark.skip(reason="Тест в разработке")
def test_tour_skipped():
    """Пропущенный тест"""
    assert True