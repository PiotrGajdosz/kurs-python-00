# produkty sklepu jako lista slownikow
shop_products = [
    {
        "name": "butter",
        "quantity": 20,
        "price": 7
    },
    {
        "name": "apple",
        "quantity": 34,
        "price": 1.2
    }
]
# produkty sklepu jako slownik slownikow
products = {
    "egg": {
        "amount": 50,
        "price": 0.8
    },
    "milk": {
        "amount": 30,
        "price": 3.9
    }
}


def update_quantity(product_name, ordered_quantity):
    for item in shop_products:
        if item["name"] == product_name:
            if item["quantity"] >= ordered_quantity:
                item.update({"quantity": item.get("quantity") - ordered_quantity})
            else:
                item.update({"quantity": 0})

# dla slownika slownikow


def update_amount(product_name, ordered_amount):
    if products[product_name]["amount"] >= ordered_amount:
        products[product_name]["amount"] -= ordered_amount
    else:
        products[product_name]["amount"] = 0


def get_price(product_name):
    for item in shop_products:
        if item.get("name") == product_name:
            return item.get("price")
