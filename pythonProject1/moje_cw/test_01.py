products = {
    "bread": {
        "amount": 20,
        "price": 9
    },
    "eggs": {
        "amount": 119,
        "price": 1.9
    },
    "water": {
        "amount": 45,
        "price": 4.5
    }
}


orders = {
    "bread": {
        "amount": 4,
        "cost": 36
    }
}


def update_amount(prod_name, prod_amount):
    if products[prod_name]["amount"] >= prod_amount:
        products[prod_name]["amount"] -= prod_amount
    else:
        products[prod_name]["amount"] = 0


def get_price(product_name):
    return products[product_name]["price"]


def new_order(prod_name, prod_amount, cost):
    order = {
        prod_name: {
            "amount": prod_amount,
            "cost": cost * prod_amount
        }
    }
    orders.update(order)


print("Produkty: ", products)
print("Zamówienia: ", orders)

name = input("Podaj nazwę produktu: ")
amount = int(input("Podaj ilość: "))

update_amount(name, amount)
new_order(name, amount, get_price(name))

print("Produkty: ", products)
print("Zamówienia: ", orders)