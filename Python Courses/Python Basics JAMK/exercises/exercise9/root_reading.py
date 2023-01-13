import os # second option
import os.path
#from os import listdir # used in first option
#from os.path import isfile, join # used in first option


#### first option
#cdrivefiles = [f for f in listdir("C:/") if isfile(join("C:/", f))]
#print(cdrivefiles)


#######

# os.chmod seems to work used with numerical values os.chmod("/tmp/test_file", "with decimal numerical permission")


#######

# second option, though they have different outputs
path_toscan = "C://"

file_list = os.listdir(path_toscan)
print(file_list)


# create file
filename = "ayho.txt"

try:
    file = open("C:\\" + filename , "w")
    file.close()
except PermissionError:
    print("Failed to create")
    
# yep it fails. 

# write somewhere we are allowed
path = os.path.expanduser("~/Desktop/") # I wanted to save on the desktop.
if not os.path.exists(path): os.makedirs(path)


file2 = open(path + filename, "w")