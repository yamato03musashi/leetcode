#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:

    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }

        romanList = list(s)
        print(romanList)
        i = 0
        num = 0
        if len(s) == 1:
            return romanDict[s]
        while i < len(s):
            # print(i)
            if i == len(s) - 1:
                num += romanDict[romanList[i]]
                i += 1
                continue
            romanSets = romanList[i] + romanList[i+1]
            if romanSets in romanDict:
                num += romanDict[romanSets]
                i += 2
                continue
            num += romanDict[romanList[i]]
            i += 1
        return num
            

# @lc code=end

# 呼び出し
solution = Solution()
print(solution.romanToInt("III"))
