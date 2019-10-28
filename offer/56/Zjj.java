/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
public class Solution {
    public ListNode deleteDuplication(ListNode pHead)
    {
        if (pHead == null || pHead.next == null) {
            // 只有0个或1个结点，直接返回
            return pHead;
        }
        if (pHead.val == pHead.next.val){
            // 当前结点和下一个节点是重复结点
            ListNode temNode = pHead.next;
            while (temNode != null && temNode.val == pHead.val){
                // 跳过相同的节点
                temNode = temNode.next;
            }
            return deleteDuplication(temNode); // 继续递归第一个和当前节点不同的点
        }else {
            // 当前结点和下一个节点不是重复结点
            pHead.next = deleteDuplication(pHead.next); //从下一个结点开始递归
            return pHead;
        }

    }
}