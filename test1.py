import random
import os 
filenum =  random.randint(0,1000)
filenum = str(filenum)
print("the file is : list"+filenum+" ")
listfile = "list"+filenum+".txt"
with open(listfile ,'w') as file:
    file.write("hello")