def sum_numbers(numbers=None):
    if numbers is None:

        total = sum(range(1, 101))
        return total

    else:
        
        return sum(numbers)
pass

numbers = range(1, 11)
numbers = [1, 2, 3, 5, 8]
numbers = None
sum_numbers(numbers)
