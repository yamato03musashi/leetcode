#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0

        for i in range(32):
            # 1. n & 1: 元の数の一番右のビットを取り出す
            last_bit = n & 1
            # 2. reversed_num << 1: 今までの結果を左に1つずらして、
            #    右端に新しいビットを入れるスペースを作る
            left_shift_num = reversed_num << 1
            # 3. |: 取り出したビットを新しい数の右端に追加する
            reversed_num = left_shift_num | last_bit
            n >>= 1
        # 処理済みのビットを右にシフトして捨てる
        return reversed_num
# @lc code=end

