def transpose_rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[0])):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    ans=[]
    for row in matrix:
        ans.append(row[::-1])
    # print(ans)
    return ans

def main(matrix,n):
    if n==0 or n//90==0:
        a=matrix
    elif n//90==1:
        a=transpose_rotate(matrix)
    elif n//90==2:
        a=transpose_rotate(transpose_rotate(matrix))
    else:
        a=transpose_rotate(transpose_rotate(transpose_rotate(matrix)))
    
    for row in a:
        print(*row)


n = int(input())
matrix = []
for i in range(n):
    x = list(map(int,input().split()))
    matrix.append(x)
# print(matrix)
angle = int(input())
(main(matrix,angle))