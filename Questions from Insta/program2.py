'''
PATTERN 
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
'''

for i in range(1,6):
    w=i
    for j in range(1,6):
        if w<6:
            print(w,end=" ")
        else:
            print((w)%5,end=" ")
        w+=1
    print()