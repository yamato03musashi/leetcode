#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #ベースケース
            return root
        self.invertTree(root.left) #左部分木を呼び出す
        self.invertTree(root.right) #右部分木を呼び出す
        # ノードを交換
        root.left, root.right = root.right, root.left
        return root #ルートを返す        
# @lc code=end

