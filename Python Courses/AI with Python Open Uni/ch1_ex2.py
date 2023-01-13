"""In the second exercise the idea is to create a small grocery shopping list with the list datastructure.
In short, create a program that allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit.


If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the list. 
If the user decides to remove something, the program informs the user about how many items there are on the list (There are [number] items in the list.") and prompts the user for the removed item ("Which item is deleted?: "). 
If the user selects 0, the first item is removed. When the user quits, the final list is printed for the user "The following items remain in the list:" followed by the remaining items one per line. 
If the user selects anything outside the options, including when deleting items, the program responds "Incorrect selection.". When the program works correctly it prints out the following:"""

shopping_list = []
option = ""

while option != 3:
    option = int(input("""Would you like to
(1) Add or
(2) Remove items or
(3) Quit?: """))
    if option > 3:
        print("Incorrect selection.")

    if option == 1:
        add_to = input("What will be added?: ")
        shopping_list.append(add_to)

    if option == 2:

        print("There are", len(shopping_list), "items in the list.")
        # print(list_len.format(len(shopping_list)))
        to_remove = int(input("Which item is deleted?: "))

        if to_remove >= len(shopping_list):
            print("Incorrect selection.")
        else:
            del shopping_list[to_remove]

    if option == 3:
        print("The following items remain in the list:")
        for i in shopping_list:
            print(i)
