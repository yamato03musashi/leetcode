#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    # 回答１
    def majorityElement(self, nums: List[int]) -> int:
        # 要素の出現回数を記録するためのハッシュマップを作成
        # defaultdict(int)を使うことで、新しいキーの初期値が0になります
        m = defaultdict(int)
        
        # 配列の長さを取得
        n = len(nums)
        
        # 各要素の出現回数をカウント
        for num in nums:
            m[num] += 1  # numという要素の出現回数を1増やす
        
        # 過半数の基準値を計算
        n = n // 2
        
        # ハッシュマップの各要素を確認
        for key, value in m.items():
            # もし出現回数が過半数を超えていたら、その要素を返す
            if value > n:
                return key
        
        return 0  # 多数要素が見つからなかった場合（この問題では実際には起こりません）        

    # 回答2
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

# @lc code=end

