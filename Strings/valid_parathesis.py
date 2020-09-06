class Solution:
    def isValid(self, s: str) -> bool:
        t=list()
        t.append(0)
        for i in range(len(s)):
            #print(s[i])
            if t[-1]=="(" and s[i]==")":
                #print("previous 1 matched")
                t.pop(-1)
            elif t[-1]=="[" and s[i]=="]":
                #print("previous 1 matched")
                t.pop(-1)
            elif t[-1]=="{" and s[i]=="}":
                #print("previous 1 matched")
                t.pop(-1)
            else:
                #print("previous one did not match, appending")
                t.append(s[i])
            #print("t now ",t)
        if len(t)<=1:
            return True
        else:
            return False
        