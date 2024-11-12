#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ダミーノードを作成し、現在のポインタ(cur)として使用
        cur = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1 # 現在のノードの次をlist1に設定
                cur = list1 # curを更新
                list1 = list1.next # list1を次に進め
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        

# @lc code=end

