#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    def __init__(self):
        # メインスタック：要素の追加用
        self.stack1 = []
        # 補助スタック：要素の取り出し用
        self.stack2 = []
        
    def push(self, x: int) -> None:
        # 新しい要素は常にstack1に追加
        self.stack1.append(x)
    
    def _transfer(self) -> None:
        # stack2が空の場合のみ、stack1の要素を全てstack2に移動
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
    
    def pop(self) -> int:
        # stack2にデータを移動し、先頭要素を取り出す
        self._transfer()
        return self.stack2.pop()
    
    def peek(self) -> int:
        # stack2にデータを移動し、先頭要素を参照する
        self._transfer()
        return self.stack2[-1]
    
    def empty(self) -> bool:
        # 両方のスタックが空の場合、キューは空
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

