# the simple way to do it is with the brute force method of looping through the string and counting 1s; complexity however is O(n)

#The method used here is the Brian Kernighan’s Algorithm which has complexity of O(log n)
#Think about it, Google for the explaination on the algorithm

class Solution:
    def hammingWeight(self, n: int) -> int:
        return(find_1s(n))
        
def find_1s(n:int)->int:
    if(n==0):
        return 0
    else:
        return 1+find_1s(n&(n-1))
