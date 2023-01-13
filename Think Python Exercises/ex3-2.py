def do_twice(print_twice, x):
    print_twice(x)
    print_twice(x)
    
def print_twice(x):
    print(x)
    



def do_four(do_twice, x):
    do_twice(print_twice, x)
    do_twice(print_twice, x)

do_twice(print_twice, "alalala")
print('')
do_four(do_twice, "alalala")