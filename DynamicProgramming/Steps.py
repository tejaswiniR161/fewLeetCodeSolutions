""" memo=[-1]*4

def count_steps(n:int)->int:
    if n==-1:
        return 0
    elif n==0:
        return 1
    else:
        if memo[n]!=-1:
            return memo[n]
        else:
            memo[n]=count_steps(n-1)+count_steps(n-2)
            return memo[n]

print(count_steps(3)) """

#Accepted answer
class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[-1]*(n+1)
        return count_steps(n,memo)

def count_steps(n:int,memo)->int:
    if n==-1:
        return 0
    elif n==0:
        return 1
    else:
        if memo[n]!=-1:
            return memo[n]
        else:
            memo[n]=count_steps(n-1,memo)+count_steps(n-2,memo)
            return memo[n]