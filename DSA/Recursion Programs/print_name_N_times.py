def printName(Name,count):
    if count == 0:
        return 
    print(Name,end=" ")
    printName(Name,count-1)

printName("Deeraj Kumar",5)