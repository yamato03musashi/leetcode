#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XORを使用した実装
        xor = 0
        for num in nums:
            xor ^= num  # 累積XOR
        
        return xor  # 単一の要素が残る
            
# @lc code=end

