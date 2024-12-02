#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:    
        # 次の数を計算する補助関数
        def get_next_number(n):    
            output = 0
            
            # 各桁の二乗を合計する
            # intを一と桁ずつトラ出す場合は%10で余を出す→//10で最後の桁を削除
            while n:
                digit = n % 10        # 最後の桁を取得
                output += digit ** 2   # その桁の二乗を加算
                n = n // 10           # 最後の桁を削除
            
            return output

        # 遅いポインタと速いポインタを初期化
        slow = get_next_number(n)
        fast = get_next_number(get_next_number(n))  # 2回計算

        # 二つのポインタが出会うまで繰り返す
        while slow != fast:
            if fast == 1:  # 速いポインタが1に到達したら、それはHappy Number
                return True
            
            # 遅いポインタは1回、速いポインタは2回進む
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))

        # ループを抜けた時点で、1であればHappy Number
        return slow == 1
        
# @lc code=end

