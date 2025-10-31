# Dicionário de estoque com quantidade, preço e preço com desconto.
inventory = {
    "Bread": [42, 1.20, 0.99],
    "Eggs": [225, 2.12, 1.99],
    "Apples": [9, 1.50, 1.35]
}

for item in inventory:
    stock = inventory[item][0]
    regular_price = inventory[item][1]
    discounted_price = inventory[item][2]

    if stock < 30:
        print(f"{item} need restocking.")
    elif stock > 100:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    elif 30 <= stock <= 100:
        print(f"{item} should be sold at the regular price of {regular_price}.")