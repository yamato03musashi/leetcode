#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        num = 0
        
        def countNode(r):
            nonlocal num  # numを内部関数で変更可能にする
            if not r:
                return
            num += 1
            countNode(r.left)
            countNode(r.right)
            
        countNode(root)
        return num
# @lc code=end

