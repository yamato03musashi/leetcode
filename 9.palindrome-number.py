#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revert = 0
        while x > revert:
            revert = revert * 10 + x % 10
            x //= 10
        return x == revert or x == revert // 10
        
# @lc code=end
