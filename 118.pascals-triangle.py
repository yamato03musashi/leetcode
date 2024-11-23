#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # 結果を格納するリストを事前に確保
        triangle = [[1] * (i + 1) for i in range(numRows)]
        
        # 3行目から計算を開始
        for i in range(2, numRows):
            for j in range(1, i):
                # 前の行の隣接する要素を加算
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        return triangle
            
# @lc code=end

# 呼び出し
solution = Solution()
print(solution.generate(5))

