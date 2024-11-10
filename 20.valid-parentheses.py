#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 空のスタックを初期化
        stack = []
        
        # 閉じ括弧と開き括弧の対応関係を定義
        bracket_map = {
            ')': '(',  # 閉じ括弧 ')' は開き括弧 '(' に対応
            '}': '{',  # 閉じ括弧 '}' は開き括弧 '{' に対応
            ']': '['   # 閉じ括弧 ']' は開き括弧 '[' に対応
        }
        
        for str in s:
            # 閉じ括弧の場合
            if str in bracket_map:
                # スタックの開き括弧を取得
                topElement = stack.pop() if stack else "#"
                # スタックの開き括弧が閉じ括弧と対応していない場合はFalse
                if topElement != bracket_map[str]:
                    return False

            else:
                stack.append(str)
        return not stack
        
# @lc code=end

