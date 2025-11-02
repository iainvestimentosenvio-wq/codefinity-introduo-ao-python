# 1. Definição da função
def calculate_total_cost(price, quantity):
    total_cost = price * quantity
    return total_cost

# 2. Chamada da função e impressão do resultado
apples_total_cost = calculate_total_cost(1.50, 10)
print(f"The total cost for apples is ${apples_total_cost}")