#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strList = s.split(' ')
        strList = [i for i in strList if i not in '']
        return len(strList[-1])
# @lc code=end

# 呼び出し
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
