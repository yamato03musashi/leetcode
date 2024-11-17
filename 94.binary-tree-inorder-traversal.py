#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def inorder(root):
            if not root:
                return
            # 左部分木を処理
            print(root.val)
            inorder(root.left)
            # 現在のノードの値を追加
            res.append(root.val)
            # 右部分木を処理
            inorder(root.right)
        
        inorder(root)
        return res
        
# @lc code=end

# 呼び出し
solution = Solution()
print(solution.inorderTraversal([1,None,2,3]))

