def transpose(matrix):
    n=len(matrix)
    m=len(matrix[0])
    transpose=[[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transpose[j][i]=matrix[i][j]
    
    return transpose


A = [[ [1, 1, 1, 1], 
 [2, 2, 2, 2], 
 [3, 3, 3, 3], 
 [4, 4, 4, 4]] ,

[[1,2],[2,3],[3,4]]]

for mat in A:
    ans=transpose(mat)
    for row in ans:
        print(row)
    print()

