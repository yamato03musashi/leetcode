#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 結果を格納するリストを1で初期化
        res = [1]
        # 前の要素を保持する変数
        prev = 1
        
        # k=1からrowIndexまでループ
        for k in range(1, rowIndex + 1):
            # 次の要素を計算
            # prev * (rowIndex - k + 1) / k の整数部分を取得
            next_val = prev * (rowIndex - k + 1) // k
            # 結果リストに追加
            res.append(next_val)
            # 次の計算のためにprevを更新
            prev = next_val
            
        return res
        
# @lc code=end


# パスカルの三角形における二項係数の関係を段階的に説明していきます：

# **1. 基本的な理解**
# 例えば、4行目（n=4）を考えてみましょう：
# ```
# [1, 4, 6, 4, 1]
# ```
# これは二項係数で表すと：
# ```
# C(4,0), C(4,1), C(4,2), C(4,3), C(4,4)
# ```

# **2. 数式での表現**
# C(n,k) = n! / (k! × (n-k)!)

# **3. 隣接する要素の関係**
# 例えば、C(4,1)からC(4,2)への変化を見てみましょう：

# C(4,1) = 4!/(1! × 3!) = 4
# C(4,2) = 4!/(2! × 2!) = 6

# **4. 変換式の導出**
# C(n,k)からC(n,k+1)への変換を一般化します：

# 1. C(n,k+1) = n! / ((k+1)! × (n-(k+1))!)
# 2. C(n,k) = n! / (k! × (n-k)!)

# これらの比を取ると：
# ```
# C(n,k+1)   n! × k! × (n-k)!
# --------- = ---------------------
# C(n,k)     (k+1)! × (n-(k+1))! × n!

#         = (n-k) / (k+1)
# ```

# **5. コードでの実装との対応**
# ```python
# next_val = prev × (rowIndex - k + 1) / k
# ```
# この式は上記の関係を実装したものです：
# - rowIndex は n に対応
# - k は現在の位置
# - prev は C(n,k-1) の値
