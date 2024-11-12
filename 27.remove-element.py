#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[k] == val:
                matchNum = nums.pop(k)
                nums.append(matchNum)
            else:
                k += 1
        return k

# @lc code=end

# 呼び出し
solution = Solution()
print(solution.removeElement([2], 3))
