import os.path

try:
    filename = "names.txt"
    path = os.path.expanduser("~/Desktop/names") # I wanted to save on the desktop.
    if not os.path.exists(path): os.makedirs(path)
    path += "/"
    file = open(path + filename, "a+")
except:
    print("Failed to create")


while True:
    name = input("Please enter a name: ")
    try:
        file.writelines(''.join(name) + '\n')
    except:
        print("Failed to write")    
    if name != '':
        continue
    elif name == '':
        file = open(path + filename, "r")
        names = [""]
        names = file.readlines()
        print(*names, sep='\n')
        file.close()
        break    

    
  