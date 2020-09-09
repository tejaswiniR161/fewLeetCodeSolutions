matrix=[[1,0,1],[1,1,1],[1,0,0]]

def set_zero(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
        
    rowflags=[False]*rows
    columnflags=[False]*columns
        
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j]==0:
                rowflags[i]=True
                columnflags[j]=True
    print("rows flags ",rowflags)
    print("column flags ",columnflags)
        
    for i in range(0,rows):
        if rowflags[i]==True:
            for j in range(0,columns):
                matrix[i][j]=0

    print("Matrix after changing rows")
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j],end=" ")
        print()

    for j in range(0,columns):
        if columnflags[j]==True:
            for i in range(0,rows):
                matrix[i][j]=0
        
    print("Matrix after changing columns")
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j],end=" ")
        print()

set_zero(matrix)        