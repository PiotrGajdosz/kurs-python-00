from products import products

orders = [
    {
        "name": "butter",
        "quantity": 2,
        "total_cost": 14
    }
]


def new_order(name, quantity, price):
    order = {
        "name": name,
        "quantity": quantity,
        "total_cost": quantity * price
    }
    orders.append(order)


def add_order(name, amount):
    order = {
        "name": name,
        "quantity": amount,
        "total_cost": products[name]["price"] * amount
    }
    orders.append(order)
