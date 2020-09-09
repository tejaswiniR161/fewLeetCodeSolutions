#rotate a matrix by 90*, it's a square matrix
matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def rotate(matrix):
    n=len(matrix)
    t=0
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    print("Transpose")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()
    
    for i in range(n):
        for j in range(0,int(n/2)):
            t=matrix[i][j]
            matrix[i][j]=matrix[i][n-j-1]
            matrix[i][n-j-1]=t

    print("rotated")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()

    

rotate(matrix)