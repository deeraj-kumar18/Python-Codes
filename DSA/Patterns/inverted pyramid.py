def inverted_pyramid(n):
    ans=[]
    for i in range(n,0,-1):
        ans.append("*"*i)
        # print("*"*i,end=" ")
    return ans

n=7
print(inverted_pyramid(n))

