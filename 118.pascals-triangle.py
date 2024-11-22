#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascalsTriangle = []
        for i in range(numRows):
            print("i",i)
            row = []
            if i == 0:
                row = [1]
            elif i == 1:
                row = [1,1]
            else:
                row = [1,1]
                for j in range(i-1):
                    print("j",j)
                    print("pascalsTriangle[i-1]",pascalsTriangle[i-1])
                    left = pascalsTriangle[i-1][j]
                    print("left",left)
                    right = pascalsTriangle[i-1][j+1]
                    print("right",right)
                    row.insert(j+1, left+right)
                    print("row",row)
            pascalsTriangle.append(row)
        return pascalsTriangle
            
# @lc code=end

# 呼び出し
solution = Solution()
print(solution.generate(5))

