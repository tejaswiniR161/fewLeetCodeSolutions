#rotate a matrix by 90*, it's a square matrix

""" n=int(input("Enter the size of n : "))
matrix=[]
for i in range(0,n):
    row=[]
    for j in range(0,n):
        #print("i,j ",i,j)
        row.append(int(input("Enter the element")))
    matrix.append(row)

print("Before rotating : ")       
for i in range(0,n):
    for j in range(0,n):
        #print("i,j ",i,j)
        print(matrix[i][j]," ",end="")
    print() """
""" matrix=[[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix)
tn=n
for i in range(0,int(n/2)):
    print("top")
    top=[j for j in matrix[i]]
    print(top)
    print("bottom")
    bottom=[j for j in matrix[n-i-1]]
    print(bottom)
    print("right")
    right=[j[n-1-i] for j in matrix]
    print(right)
    print("left")
    left=[j[i] for j in matrix]
    print(left)

    """ 

matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

def display(matrix123):
    for i in range(len(matrix123)):
        for j in range(len(matrix123)):
            print(matrix123[i][j],end=" ")
        print()

def rotate_90(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            print("i, j",i,j)
            print(matrix[i][j])
            print(matrix[j][i])
            t=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=t
            print(" after changing i, j",i,j)
            print(matrix[i][j])
            print(matrix[j][i])
    
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()

rotate_90(matrix)