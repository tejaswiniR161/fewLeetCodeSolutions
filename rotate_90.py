#rotate given matrix by 90 degrees

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

class Solution:
    def rotate(self, matrix)#: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        templen=len(matrix)
        for i in range(0,n/2):
            temp=list()
            for j in range(0,n/2):
                temp.append(matrix[i][j])


        #rotate_here(matrix,len(matrix))

def rotate_here(matrix,l):
    n=len(matrix)
    if l==1 or l==0:
        return matrix
    t=matrix[]
    for i in range(0,n/2):
