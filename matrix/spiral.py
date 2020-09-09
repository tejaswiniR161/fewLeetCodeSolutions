matrix=[[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
matrix=[[ 1, 2, 3 ,4],[ 5, 6,7,8 ],[ 9,10,11,12 ],[13,14,15,16]]
ans=[]

def convspiral(matrix,ans,rows,columns,iter):     
    temp=[]
    for i in range(iter,rows-iter):
        if i==iter:
            for j in range(iter,columns-iter):
                print("here")
                ans.append(matrix[i][j])

        elif i!=rows-iter-1: 
            ans.append(matrix[i][columns-iter-1])
            print("temp index ",i,iter)
            if temp==[]:
                temp.append(matrix[i][iter])
            else:
                temp.insert(0,matrix[i][iter])
        
        if i==rows-iter-1 and i!=iter:
            for j in range(columns-iter-1,-1+iter,-1):
                print("here?")
                ans.append(matrix[i][j])
            for k in temp:
                ans.append(k)
                temp=[]
        #for j in range(iter,columns-iter):
    print(ans)
    if iter<int(rows/2) and iter<int(columns/2):
        convspiral(matrix,ans,len(matrix),len(matrix[0]),iter+1)
    

    

convspiral(matrix,ans,len(matrix),len(matrix[0]),0)