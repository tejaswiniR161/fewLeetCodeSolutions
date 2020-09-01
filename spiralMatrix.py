class Solution:
    def spiralOrder(self, matrix):#: List[List[int]]) -> List[int]:
        ans=list()

        r=len(matrix)
        c=len(matrix[0])


        for k in range(0,r):

            for j in range(k,c-k):
                print("k and j ",k, j)
                s=k
                t=j
                ans.append(matrix[k][j])
                print("1st ",matrix[k][j])
            for j in range(k+1,r-k-1):
                ans.append(matrix[j][c-k-1])
                print("2nd ",matrix[j][c-k-1])
            for j in range(c-k-1,k-1,-1):
                print("r-1-k = ",r-1-k," j = ",j)
                if s!=r-1-k and t!=j:
                    ans.append(matrix[r-1-k][j])
                    print("3rd ",matrix[r-1-k][j])
            for j in range(r-k-2,k,-1):
                ans.append(matrix[j][k])
                print("4th ",matrix[j][k])

        return ans
        
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
s=Solution()
print(s.spiralOrder(matrix))

#matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
#print_spiral(5,4,matrix)