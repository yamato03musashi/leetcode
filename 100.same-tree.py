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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_traversal = []
        q_traversal = []
        def traversal_p(t: Optional[TreeNode]):
            if not t:
                return
            traversal_p(t.left())
            p_traversal.append(t.val)
            traversal_p(t.right())

        def traversal_q(t: Optional[TreeNode]):
            if not t:
                return
            traversal_q(t.left())
            q_traversal.append(t.val)
            traversal_q(t.right())


        traversal_p(p)
        traversal_q(q)
        if p_traversal == q_traversal:
            return True
        return False
           



# @lc code=end

