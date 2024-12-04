#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 空リストまたは1要素の場合はそのまま返す
        if not head or not head.next:
            return head
            
        # 再帰関数の定義
        def reverse(cur: ListNode) -> ListNode:
            # ベースケース：最後のノードに到達
            if not cur.next:
                return cur
                
            # 再帰的に次のノードを処理し、新しいheadを取得
            new_head = reverse(cur.next)
            
            # ポインタの付け替え
            cur.next.next = cur  # 次のノードのnextを現在のノードに向ける
            cur.next = None      # 現在のノードのnextをNoneに設定
            
            return new_head
            
        # 再帰関数を実行して新しいheadを返す
        return reverse(head)

# """
# 動作例 ([1,2,3,4,5]の場合):

# 1. 最初のreverse(1)呼び出し
#    -> reverse(2)呼び出し
#       -> reverse(3)呼び出し
#          -> reverse(4)呼び出し
#             -> reverse(5)呼び出し
#                5.next がないのでreturn 5

# 2. ポインタの付け替え（逆順に実行）:
#    4.next.next = 4  # 5.next = 4
#    4.next = None    # 5->4

#    3.next.next = 3  # 4.next = 3
#    3.next = None    # 5->4->3

#    2.next.next = 2  # 3.next = 2
#    2.next = None    # 5->4->3->2

#    1.next.next = 1  # 2.next = 1
#    1.next = None    # 5->4->3->2->1

# 結果: 5->4->3->2->1
# """

# @lc code=end

