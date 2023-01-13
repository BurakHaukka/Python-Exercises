balance = 2000

print(balance, "Euros")

deposit = int(input("How many Euros you want to deposit ?: "))

deposit_cent = int(input("How many cents you want to deposit ?: ")) / 100

balance = balance + deposit + deposit_cent

print(balance)