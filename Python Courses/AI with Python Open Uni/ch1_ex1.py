"""This exercise tests out the default values of parameters. Create a program which has a main function and a subfunction called tester.

The main function prompts user for an input "Write something (quit ends): " and sends this input to the subfunction as a parameter. 

Define the subfunction tester so that it has one parameter called "givenstring", which has the default value "Too short".

If the user input is less than 10 characters, the program uses the default value and if 10 or more, it prints the usergiven input.

If the user inputs "quit", the program is terminated. When working correctly, the program will print out something like this:"""

def tester(user_input):
    
    givenstring = "Too Short"
    
    if len(user_input) < 10:
        print(givenstring)
    else:
        print(user_input)
        
def main():
    
    user_input = ""
    
    while user_input != "quit":
        user_input = input("Write something (quit ends): ")
        if user_input == "quit":
            print("Quitting !")
            break
        
        tester(user_input)
main()