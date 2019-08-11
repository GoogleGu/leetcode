public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}

public class Solution {
    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if (pHead1 == null || pHead2 == null) {
            return null;
        }
        int pLen1 = getListNodeLength(pHead1);
        int pLen2 = getListNodeLength(pHead2);
        int diff = pLen1 - pLen2;
        if (diff > 0) {
            while (diff > 0) {
                pHead1 = pHead1.next;
                diff--;
            }
            while (pHead1 != pHead2) {
                pHead1 = pHead1.next;
                pHead2 = pHead2.next;
            }
            return pHead1;
        } else {
            while (diff < 0) {
                pHead2 = pHead2.next;
                diff++;
            }
            while (pHead1 != pHead2) {
                pHead1 = pHead1.next;
                pHead2 = pHead2.next;
            }
            return pHead1;
        }
    }
// 得到长度
    public Integer getListNodeLength(ListNode ln) {
        int count = 0;
        while (ln != null) {
            count++;
            ln = ln.next;
        }
        return count;
    }
}