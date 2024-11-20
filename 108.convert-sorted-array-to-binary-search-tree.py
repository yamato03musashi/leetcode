#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 空配列の場合はNoneを返す
        if not nums:
            return None
            
        # 配列の中心を取得
        mid = len(nums) // 2
        # 中心の値でノードを作成
        root = TreeNode(nums[mid])
        
        # 配列を分割して左右の部分木を作成
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root
        
# @lc code=end

