import pytest
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE
from Diplom_1.ingredient_types import INGREDIENT_TYPE_FILLING

class TestIngredient:
    # Тест получения цены
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'chili sauce', 300)
        assert ingredient.get_price() == 300

    # Тест получения названия
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'dinosaur', 200)
        assert ingredient.get_name() == 'dinosaur'

    # Тест получения типа
    @pytest.mark.parametrize(
        'type, name, price, ERingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'hot sauce', 100, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'cutlet', 100, 'FILLING']
        ]
    )

    def test_get_type(self, type, name, price, ERingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == ERingredient