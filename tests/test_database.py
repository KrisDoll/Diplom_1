import pytest
from Diplom_1.database import Database


class TestDatabase:
    # Тест доступных булочек
    @pytest.mark.parametrize("name, price", [(["black bun", "white bun", "red bun"], [100, 200, 300])])
    def test_available_buns(self, name, price):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    # Тест доступных ингредиентов
    @pytest.mark.parametrize("name, price", [(["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"], [100, 200, 300, 100, 200, 300])]                       )
    def test_available_ingredients(self,name, price):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
