#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            # 一致したら抜ける
            while not s.startswhith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
# @lc code=end

