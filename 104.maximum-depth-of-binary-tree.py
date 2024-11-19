#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        # ベースケース：空の木の場合
        if not root:
            return 0
            
        # 左部分木の最大深さを計算
        left_depth = self.maxDepth(root.left)
        # 右部分木の最大深さを計算
        right_depth = self.maxDepth(root.right)
        
        # 左右の深さの大きい方に1を加える（現在のノードの分）
        return max(left_depth, right_depth) + 1

# @lc code=end

