from collections import Counter # this Counter from collections library counts occurences

try:
    filename = "names.txt"
    file = open(filename, "r")
    names = file.readlines()
except:
    print("Failed to read")
finally:
    file.close()

names_split = []

for name in names:
    names_split.extend(name.split()) 

names_split.sort()
print(names_split)
print(Counter(names_split))
