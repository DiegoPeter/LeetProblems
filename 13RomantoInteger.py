class Solution:
    def romanToInt(self, s: str) -> int:
        dict={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res=0
        for i in range(0,len(s)-1):
            if s[i]=='I' and s[i+1]=='V':
                res-=dict[s[i]]
            elif s[i]=='I' and s[i+1]=='X':
                res-=dict[s[i]]
            elif s[i]=='X' and s[i+1]=='L':
                res-=dict[s[i]]
            elif s[i]=='X' and s[i+1]=='C':
                res-=dict[s[i]]
            elif s[i]=='C' and s[i+1]=='D':
                res-=dict[s[i]]
            elif s[i]=='C' and s[i+1]=='M':
                res-=dict[s[i]]
            else:
                res+=dict[s[i]]
        return res+dict[s[-1]]