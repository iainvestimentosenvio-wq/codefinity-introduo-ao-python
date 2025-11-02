def apply_discount(prices):
    prices_copy = prices.copy()
    for i in range(len(prices_copy)):
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.90
    return prices_copy

# Lista de preços
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Chama a função e armazena o resultado
updated_prices = apply_discount(product_prices)

# Imprime o resultado
print(f"Updated product prices: {updated_prices}")
