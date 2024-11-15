#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        prev1 = 1  # F(n-2)
        prev2 = 2  # F(n-1)
        
        for i in range(3, n + 1):
            current = prev1 + prev2  # F(n) = F(n-1) + F(n-2)
            prev1 = prev2
            prev2 = current
            
        return prev2


# @lc code=end

# 基本的な考え方:

# n段目に到達する方法は、(n-1)段目から1段上がる方法と
# (n-2)段目から2段上がる方法の合計となります


# 漸化式:
# CopyF(n) = F(n-1) + F(n-2)
# ここで、

# F(n) = n段目に到達する方法の総数
# F(n-1) = (n-1)段目に到達する方法の総数
# F(n-2) = (n-2)段目に到達する方法の総数


# 初期条件:
# CopyF(1) = 1 (1段の場合は1通り)
# F(2) = 2 (2段の場合は2通り)

# 具体的な計算例:
# n = 3 の場合:
# CopyF(3) = F(2) + F(1)
# F(3) = 2 + 1 = 3
# n = 4 の場合:
# CopyF(4) = F(3) + F(2)
# F(4) = 3 + 2 = 5


# n:     1, 2, 3, 4, 5,  6,  7,  8,  9...
# F(n):  1, 2, 3, 5, 8, 13, 21, 34, 55...
