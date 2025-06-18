import pytest
from Diplom_1.bun import Bun

class TestBun:
    # Тест получения корректного названия
    def test_get_name(self):
        bun = Bun('black bun', 100)
        assert bun.get_name() == 'black bun'

    # Тест получения корректной цены
    def test_get_price(self):
        bun = Bun('white bun', 200)
        assert bun.get_price() == 200