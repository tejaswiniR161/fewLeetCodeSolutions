class Solution:
    def intToRoman(self, num: int) -> str:
        n=str(num)
        answer=""
        dict={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        for i in range(0,len(n)):
            ns=list(n[i:len(n)])
            current=int(n[i])
            #print("current element and length",current,len(ns))
            len1=str(1)+(str("0"*(len(ns)-1)))
            #print("len1 : ",len1)
            if current<=3 and current>=1:
                answer=answer+(dict[1*int(len1)]*current)
            elif current==4 or current==9:
                if current==4:
                    answer=answer+dict[1*int(len1)]+dict[5*int(len1)]
                if current==9:
                    #answer=answer+dict[1*int(len1)]+dict[1*int(len1)]
                    answer=answer+dict[1*int(len1)]+dict[1*int(len1)*10]
            elif current==5:
                answer=answer+dict[5*int(len1)]
            elif current>=6 and current<=8:
                answer=answer+dict[5*int(len1)]+(dict[1*int(len1)]*(current%5))
        return(answer)       
s=Solution()
print(s.intToRoman(9))  