#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = {
            "A":1,
            "B":2,
            "C":3,
            "D":4,
            "E":5,
            "F":6,
            "G":7,
            "H":8,
            "I":9,
            "J":10,
            "K":11,
            "L":12,
            "M":13,
            "N":14,
            "O":15,
            "P":16,
            "Q":17,
            "R":18,
            "S":19,
            "T":20,
            "U":21,
            "V":22,
            "W":23,
            "X":24,
            "Y":25,
            "Z":26,
        }
        num = 0
        columnList = list(columnTitle)
        for i, columnStr in enumerate(columnList):
            # 解説
            # 26進数の桁数を計算する
            # 26進数の桁数は、26の累乗で表現される
            # 例えば、"AB"の場合、"A"は26の0乗、"B"は26の1乗
            # つまり、"AB"は26の0乗 + 26の1乗 = 26 + 26 = 52
            num += column[columnStr] * (26 ** (len(columnList) - i - 1))
        return num


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A"))
    print(s.titleToNumber("AB"))
    print(s.titleToNumber("ZY"))

