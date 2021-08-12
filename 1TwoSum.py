from typing import List


class Solution:
    # Complexity of O(n) where n is len(nums)
    def twoSum(self, nums: list, target: int): #Retorna o valor em qualquer ordem
        seen={}
        for index,value in enumerate(nums):
            remain=target-nums[index]
            if remain in seen:
                return index,seen[remain]
            else:
                seen[value]=index

    def twoSum2(self, nums: list, target: int): #Retorna o valor em ordem crescente
            seen={}
            for index,value in enumerate(nums):
                remain=target-nums[index]
                if remain in seen:
                    if index > seen[remain]: 
                        return seen[remain],index
                    else: 
                        return index,seen[remain]
                else:
                    seen[value]=index
 

nums=[1,5,7,9,14,-9,-15,-7]
target=-16
Slt=Solution()
print(Slt.twoSum(nums,target))
print(Slt.twoSum2(nums,target))
