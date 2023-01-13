def namelist():
    namelist = []
    namelist.append(input("Please enter a name: "))
    while True:
        if namelist[-1] != '':
            namelist.append(input("Please enter a name: "))
        elif namelist[-1] == '':
            del namelist[-1]
            print("Student count is: ", len(namelist))
            print(", ".join(namelist))
            break

namelist()
