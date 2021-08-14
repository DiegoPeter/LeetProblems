class Solution:
    def plusOne(self, digits, pos=None):

        if pos == None:
            pos = len(digits)-1
        digits[pos] += 1
        if pos == 0 and digits[pos] == 10:
            digits[pos] = 1
            digits.append(0)
        elif digits[pos] == 10:
            digits[pos] = 0
            self.plusOne(digits, pos-1)
        return digits


tst = Solution()
digits = [9, 9]
a = tst.plusOne(digits)
print(a)
