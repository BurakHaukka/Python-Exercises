
numbers = list(range(-30, 50))


# def filter_positive_even_numbers(numbers):
#     """Receives a list of numbers, and returns a filtered list of only the
#        numbers that are both positive and even (divisible by 2), try to use a
#        list comprehension."""
#     numbers = [i for i in numbers if i % 2 == 0 and i > 0]
#     return numbers
#     pass

#or

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    return [i for i in numbers if i % 2 == 0 and i > 0]
    pass

filter_positive_even_numbers(numbers)