list = ["a", "b", "c", "d", "e"]
print("""Enter blank input to stop program""")
while True:
    try:

        index = int(input("\n\nWhere do you want to insert the new value? : "))
        replace = input("\n\nWhat is the new value? : ")
        list[index] = replace
        print(list)
    except IndexError:
        print("\n\nIndex value is out of range. Range is 0 to 4.\n\n")
    except ValueError:
        print("\n\nExiting")
        break