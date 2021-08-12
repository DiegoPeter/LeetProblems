class Solution:
    def reverse(self, x: int) -> int: #Solução normal
        res=0
        if x<0:
            symbol=-1
            x=-x
        elif x>0:
            symbol=1
        else:
            return x
        
        while(x!=0):
            res=res*10 + x%10
            x = x//10
        
        if symbol==1:
            return 0 if res>pow(2,3)-1 else res
        else: 
            return 0 if res>pow(2,31) else res*symbol
    
    def reverse2(self,x: int): #Solução transformando x em string
        if x < 0:
            symbol = -1
            strx=str(x)[1:]
        elif x > 0:
            symbol = 1
            strx = str(x)
        else:
            return x
        res = int(strx[::-1])
        if symbol==1:
            return 0 if res>pow(2,31)-1 else res
        else: 
            return 0 if res>pow(2,31) else res*symbol

