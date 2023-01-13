def grid_long():
    print('+ ', end='')
    print('- '*4, end='')
    print('+ ', end='')
    print('- '*4, end='')
    print('+ ')
    print('| ', ' '*6, '| ', ' '*6, '|')
    print('| ', ' '*6, '| ', ' '*6, '|')
    print('| ', ' '*6, '| ', ' '*6, '|')
    print('| ', ' '*6, '| ', ' '*6, '|')
    print('+ ', end='')
    print('- '*4, end='')
    print('+ ', end='')
    print('- '*4, end='')
    print('+ ')
    print('| ', ' '*6, '| ', ' '*6, '|')
    print('| ', ' '*6, '| ', ' '*6, '|')
    print('| ', ' '*6, '| ', ' '*6, '|')
    print('| ', ' '*6, '| ', ' '*6, '|')
    print('+ ', end='')
    print('- '*4, end='')
    print('+ ', end='')
    print('- '*4, end='')
    print('+ ')
    print(' '*4)
    print('**** END ****')
grid_long()


## using more functions to make 4x4 grid

def print_twice():
    print()
    print()
    
def do_twice(print_twice):
    print_twice()
    print_twice()
    
def do_four(x):
    do_twice(x)
    do_twice(x)
    
def grid_beam():
    print('+ - - - - ', end='')
    
    
def grid_pole():
    print('|         ', end='')
    
    
def print_beams():
    do_twice(grid_beam)
    

def print_poles():
    do_twice(grid_pole)
    
    
def grid_function(print_beams, print_poles):
    do_twice(print_beams)
    print('+')
    do_four(grid_pole)
    print('|')
    do_four(grid_pole)
    print('|')
    do_four(grid_pole)
    print('|') 
    do_four(grid_pole)
    print('|')

def grid_4x4(print_beams, print_poles):
    grid_function(print_beams, print_poles)
    grid_function(print_beams, print_poles)
    grid_function(print_beams, print_poles)
    grid_function(print_beams, print_poles)
    do_twice(print_beams)
    print('+')

grid_4x4(print_beams, print_poles)