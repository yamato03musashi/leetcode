#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            # haystackの0からneedle文字分の文字列が一致しているか見ればよい
            # それを１文字ずつずらしていく
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1 
    # @lc code=end
