#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        return (self.Height(root) >= 0)
        
    def Height(self, root, depth=0):  # depthパラメータを追加
        # インデントを使って現在の深さを視覚化
        indent = "  " * depth
        print(f"{indent}Checking node:", root.val if root else None)
        
        if root is None:
            print(f"{indent}Leaf node reached, returning 0")
            return 0
            
        # 左部分木の処理
        print(f"{indent}Going left from node {root.val}")
        leftheight = self.Height(root.left, depth + 1)
        print(f"{indent}Left height of {root.val} is {leftheight}")
        
        # 右部分木の処理
        print(f"{indent}Going right from node {root.val}")
        rightheight = self.Height(root.right, depth + 1)
        print(f"{indent}Right height of {root.val} is {rightheight}")
        
        # バランスチェック
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            print(f"{indent}Unbalanced at node {root.val}")
            return -1
            
        result = max(leftheight, rightheight) + 1
        print(f"{indent}Height at node {root.val} is {result}")
        return result
        
# @lc code=end

