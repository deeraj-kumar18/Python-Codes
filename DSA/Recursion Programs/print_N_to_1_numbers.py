def printNos(N):
    if N==0:
        return
    print(N,end=" ")
    printNos(N-1)

for i in range(10,0,-1):
    printNos(i)
    print()