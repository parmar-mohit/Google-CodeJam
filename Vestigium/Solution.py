import numpy as np

#print("Enter T : ",end="")
t = int(input())

for i in range(0,t):
    #print("Enter N : ",end="")
    n = int(input())
    
    mat = []
    trace = 0
    for j in range(0,n):
        #print("Enter row {} ".format(j+1),end="")
        mat.append(list(map(int,input().split(" "))))
        trace += mat[j][j]
        
    mat = np.array(mat)
    
    row = 0
    column = 0
    for k in range(0,n):
        if len(set(list(mat[k]))) < n:
            row += 1
        if len(set(list(mat[:,k]))) < n:
            column += 1
        
    print("Case #{}: {} {} {}".format(i+1,trace,row,column))