"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Cart
from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product2():
    return Product("journal", 15.25, "This is a journal", 500)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(999)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(10000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_new_product(self, cart: Cart, product: Product):
        cart.add_product(product, 5)
        assert cart.products.get(product) == 5

    def test_add_existing_product(self, cart: Cart, product: Product):
        cart.add_product(product, 3)
        cart.add_product(product, 1)
        assert cart.products.get(product) == 4

    def test_remove_product_none(self, cart: Cart, product: Product):
        cart.add_product(product, 8)
        cart.remove_product(product, None)
        assert cart.products == {}

    def test_remove_product_less(self, cart: Cart, product: Product):
        cart.add_product(product, 8)
        cart.remove_product(product, 5)
        assert cart.products[product] == 3

    def test_remove_product_more(self, cart: Cart, product: Product):
        cart.add_product(product, 8)
        cart.remove_product(product, 9)
        assert cart.products == {}

    def test_clear(self, cart: Cart, product: Product, product2: Product):
        cart.add_product(product, 8)
        cart.add_product(product2, 3)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, cart: Cart, product: Product, product2: Product):
        cart.add_product(product, 8)
        cart.add_product(product2, 16)

        price = 0
        for consume in cart.products:
            price += cart.products[consume] * consume.price

        assert cart.get_total_price() == price

    def test_buy_enough_goods(self, cart: Cart, product: Product):
        cart.add_product(product, 50)
        cart.buy()
        assert product.quantity == 950

    def test_buy_much_goods(self, cart: Cart, product: Product):
        cart.add_product(product, 1100)
        with pytest.raises(ValueError):
            cart.buy()
