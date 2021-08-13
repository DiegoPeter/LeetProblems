class Solution:
    def longestCommonPrefix(self, m) -> str:
        if not m:
            return ""
        shortest=min(m,key=len)
        for i, letter in enumerate(shortest):
            for j in m:
                if j[i] != letter:
                    return shortest[:i]
        return shortest

func=Solution()
strs = ["cir","car"]
print(func.longestCommonPrefix(strs))
