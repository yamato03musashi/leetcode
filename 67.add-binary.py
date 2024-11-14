#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aList = list(a)
        bList = list(b)
        if len(a) > len(b):
            for i in range(len(a) - len(b)):
                bList.insert(0,'0')
        elif len(b) > len(a):
            for i in range(len(b) - len(a)):
                aList.insert(0,'0')
        listLen = len(aList)
        # print(listLen)
        ansList = []
        next = 0
        print(aList)
        print(bList)
        for i in range(1, listLen + 1):
            a = int(aList[listLen - i])
            b = int(bList[listLen - i])
            sum = a + b + next
            print(sum)
            next = sum // 2
            print(next)
            current = sum % 2
            print(current)
            ansList.insert(0,str(current))
        if next == 1:
            ansList.insert(0,str(next))
        return ''.join(ansList)
    
# @lc code=end

# 呼び出し
solution = Solution()
print(solution.addBinary("11", "1"))
