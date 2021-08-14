class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            
            if mid-1>=low and nums[mid]>target:
                if nums[mid-1] < target:
                    return mid
            elif target < nums[low]:
                return low
            elif target > nums[high]:
                return high+1
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low=mid+1
            elif nums[mid] > target:
                high=mid-1
            
                
        return mid