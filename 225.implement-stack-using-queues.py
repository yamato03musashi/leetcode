#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:
    def __init__(self):
        # キューとしてdequeを初期化
        self.q = deque()

    def push(self, x: int) -> None:
        # 新しい要素をキューの後ろに追加
        self.q.append(x)
        # 新しく追加した要素以外を全て後ろに移動
        # これにより最後に追加した要素が先頭に来る
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # キューの先頭（スタックのトップ）を削除して返す
        return self.q.popleft()

    def top(self) -> int:
        # キューの先頭（スタックのトップ）を返す
        return self.q[0]

    def empty(self) -> bool:
        # キューが空かどうかを返す
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

