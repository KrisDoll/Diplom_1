import pytest
from Diplom_1.bun import Bun
from Diplom_1.burger import Burger
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE
from Diplom_1.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:

    # Тест выбора булочки
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(name="white bun", price=200)
        burger.set_buns(bun)
        assert burger.bun == bun

    # Тест добавления ингредиента
    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name="cutlet", price=100)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    # Тест удаления ингредиента
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name="cutlet", price=100)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    # Тест смены мест ингредиентов
    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, name="cutlet", price=100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, name="dinosaur", price=200)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(index=0, new_index=1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    # Тест получения цены бургера
    def test_get_price(self):
        burger = Burger()
        bun = Bun(name="red bun", price=300)
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, name="hot sauce", price=100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, name="dinosaur", price=200)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 900

    # Тест получения состава
    def test_get_receipt(self):
        burger = Burger()
        bun = Bun(name="black bun", price=100)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, name="sausage", price=300)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, name="chili sauce", price=300)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "= filling sausage =" in receipt
        assert "= sauce chili sauce =" in receipt
        assert "(==== black bun ====)" in receipt
        assert "Price:" in receipt
