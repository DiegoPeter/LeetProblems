class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx=str(x)
        if x < 0:
            return False
        elif len(strx) == 1:
            return True
        else:
            strx=str(x)
            if len(strx)%2 != 0:
                mid=len(strx)//2
                left=strx[:mid]
                right=strx[mid+1:]
                rev_right=right[::-1]
                return False if left!= rev_right else True
            else:
                mid=len(strx)//2
                if mid == 1:
                    return True if strx[0] == strx[1] else False 
                left=strx[:mid]
                right=strx[mid:]
                rev_right=right[::-1]
                return False if left!= rev_right else True