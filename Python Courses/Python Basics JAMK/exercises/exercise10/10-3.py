import ast 
import os

print("""This program separates your inputs as integer or rational number (float)\n\n
!!!! To exit the program enter blank input !!!!\n""")

while True:
    try: ###Opening files ####
        int_file = "integers.txt"
        rational_file = "rational.txt"
        path = os.path.expanduser("~/Desktop/sorted_numbers") # I wanted to save on the desktop.
        if not os.path.exists(path): os.makedirs(path)
        path += "/"
        
        int_file = open(path + int_file, "a+")
        rational_file = open(path + rational_file, "a+")
        
        
        ### Receiving user input #####
        num = ast.literal_eval(input("Enter a number: ")) # this evaluates the input and decides if it is integer or float
        
        if type(num) == int:
            try:
                
                int_file.writelines(''.join(str(num)) + '\n')
            except:
                print("Failed to write")
        if type(num) == float:
            try:
                rational_file.writelines(''.join(str(num)) + '\n')
            except:
                print("Failed to write")            
        
    except ValueError:
        print("\n\nYou cant use letters !!\n\n")
    except PermissionError:
        print("Failed to create file")
    except SyntaxError:
        print("Exiting program")
        int_file.close()
        rational_file.close()
        break

