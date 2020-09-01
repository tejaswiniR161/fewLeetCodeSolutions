class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ndividend=dividend
        ndivisor=divisor
        ndividend=abs(ndividend)
        ndivisor=abs(ndivisor)
        newdivi=ndividend
        ans=0
        print(dividend,divisor)
        while newdivi>=ndivisor:
            ans+=1
            newdivi-=ndivisor
        if dividend==0:
            return 0
        elif dividend>0 and divisor>0:
            #print("here here")
            return ans
        elif dividend<0 and divisor<0:
            #print("here here")
            return ans
        elif dividend<0 or divisor<0:
            return -1*ans

s=Solution()
print(s.divide(0,1))