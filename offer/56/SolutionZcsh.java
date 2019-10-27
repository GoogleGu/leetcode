/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
public class SolutionZcsh {
    public ListNode deleteDuplication(ListNode pHead)
    {
        if (pHead == null || pHead.next == null) return pHead;
        ListNode result = new ListNode(0);
        result.next = pHead;
        ListNode preNode = result;
        while (pHead != null) {
            if (pHead.next == null || pHead.next.val != pHead.val) {
                preNode = pHead;
                pHead = pHead.next;
                continue;
            }
            int value = pHead.val;
            while (pHead != null && pHead.val == value) {
                pHead = pHead.next;
            }
            preNode.next = pHead;
        }
        return result.next;
    }
}
