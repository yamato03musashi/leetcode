#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i

        for i in range(n):
            completion = target - nums[i]
            if completion in numMap and numMap[completion] != i:
                return [i, numMap[completion]]
        
        return []
        

# @lc code=end

