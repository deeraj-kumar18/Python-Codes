def printNos(N):
    if N==0:  # Base Condition
        return
    printNos(N-1)  # Recursive Call
    print(N,end=" ")

for i in range(11):
    printNos(i)
    print()