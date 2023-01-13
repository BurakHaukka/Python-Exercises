prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
cart = []
totalsum = 0
product = ""
print("""Supermarket
===========""")
while product != 0:
    product = int(input("Please select product (1-10) 0 to Quit: "))
    if 1 <= product <= 10:
        price_index = product - 1
        print("Product: ", product, "Price: ", prices[price_index])
        cart.append(prices[price_index])
    if product == 0:
        totalsum = sum(cart)
        print("Total: ", totalsum)
        payment = int(input("Payment:"))
        change = payment - totalsum
        print("Change: ", change)

