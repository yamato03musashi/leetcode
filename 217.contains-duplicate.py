#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        # 重複チェックはセット
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
        return False
# @lc code=end

