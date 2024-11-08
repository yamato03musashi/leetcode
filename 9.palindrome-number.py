#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(f"入力値: {x}")
        
        if x < 0 or (x % 10 == 0 and x != 0):
            print(f"負の数または末尾が0の場合は回文ではありません")
            return False
            
        revertedNumber = 0
        original = x
        print(f"数字を反転していきます...")
        
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
            print(f"現在の状態: x = {x}, 反転した数 = {revertedNumber}")
        
        # 偶数桁の場合と奇数桁の場合の2パターン
        is_palindrome = x == revertedNumber or x == revertedNumber // 10
        print(f"元の数字 {original} は回文{'' if is_palindrome else 'ではありません'}")
        
        return is_palindrome
        
# @lc code=end

# 呼び出し
solution = Solution()
print(solution.isPalindrome(1221))
