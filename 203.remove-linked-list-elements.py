#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # ダミーノードを作成（エッジケース処理のため）
        temp = ListNode(0)
        temp.next = head
        
        # 2つのポインタを初期化
        # prev: 現在のノードの前のノード
        # curr: 現在処理中のノード
        prev, curr = temp, head
        
        # リストを走査
        while curr:
            if curr.val == val:
                # 削除対象の値が見つかった場合
                # 前のノードの次の参照を、現在のノードの次のノードに変更
                # これにより現在のノードが効果的に削除される
                prev.next = curr.next
            else:
                # 削除対象でない場合は、prevポインタを進める
                prev = curr
            
            # 現在のポインタを次のノードに移動
            curr = curr.next
        
        # ダミーノードの次のノード（実際のリストの先頭）を返す
        return temp.next
# @lc code=end

