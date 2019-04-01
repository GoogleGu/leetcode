/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode FindKthToTail(ListNode head,int k) {
        ListNode result = head;
        while (head != null) {
            if (k-- <= 0)
                result = result.next;
            head = head.next;
        }
        return k > 0 ? null : result;
    }
}
