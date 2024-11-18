#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        # 両方のノードがNoneの場合、同一
        if p is None and q is None:
            return True
        # 一方のノードだけがNoneの場合、同一ではない
        if p is None or q is None:
            return False
        # 値が等しいかチェックし、左右の部分木を再帰的にチェック
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # 値が等しくない場合、同一ではない
        return False

# @lc code=end

