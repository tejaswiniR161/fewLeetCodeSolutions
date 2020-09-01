def print_spiral(r,c,matrix):
    ans=list()
    #print("matrix",matrix)
    for i in range(0,r):
        for j in range(i,c-i):
            #print(matrix[i][j])
            ans.append(matrix[i][j])
        for j in range(i,c-i):
            #print(matrix[i][j])
            ans.append(matrix[i][j])
    print("Ans: ",ans)


matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
print_spiral(5,4,matrix)