#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# ローマ数字では、小さい値が大きい値の前に現れると減算を表し,
# 小さい値が大きい値の後または等しい値の後に現れると加算を表すという直感が重要です。

# @lc code=start
class Solution:

    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num = 0

        for i in range(len(s)):
            if i < len(s) -1 and romanDict[s[i]] < romanDict[s[i+1]]:
                num -= romanDict[s[i]]
            else:
                num += romanDict[s[i]]
        return num
            

# @lc code=end

# 呼び出し
solution = Solution()
print(solution.romanToInt("III"))
