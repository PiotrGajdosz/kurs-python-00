from products import update_quantity
from products import shop_products
import products
from products import get_price
from orders import new_order
import orders


def shop():
    print("Produkty: ", products.products)
    print("Zamówienia: ", orders.orders)

    name = input("Podaj nazwe produktu: ")
    amount = int(input("Podaj ilosc: "))

    # update_quantity(name, amount)
    # new_order(name, amount, get_price(name))

    products.update_amount(name, amount)
    orders.add_order(name, amount)

    print("Produkty: ", products.products)
    print("Zamówienia: ", orders.orders)


if __name__ == "__main__":
    shop()
