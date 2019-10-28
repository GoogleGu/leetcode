public class Solution {

    public ListNode deleteDuplication(ListNode pHead) {
        if (pHead == null || pHead.next == null) {
            return pHead;
        }

        ListNode temp = pHead.next;                             // 1   2   3    3    4   4    5

        // 相同的不记录
        while (temp != null && temp.val == pHead.val) {
            temp = temp.next;
        }
        // 说明当前有重复
        if (pHead.next != temp) {
            return deleteDuplication(temp);
        }
        
        //不重复就设置下一个
        pHead.next = deleteDuplication(temp);
        return pHead;
    }
}
