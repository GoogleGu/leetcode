
class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null){return head;}
        return sort(head);
    }


    public  ListNode sort(ListNode head) {
        if (head.next == null) {
            return head;
        }
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        fast = slow.next;
        slow.next=null;
        head=sort(head);
        fast=sort(fast);
        ListNode newHead = hebing(head, fast);
        return newHead;
    }


    public ListNode hebing(ListNode left, ListNode right) {
        ListNode head;
        if (left.val<= right.val) {
            head = left;
            left = left.next;
        } else {
            head = right;
            right = right.next;
        }
        ListNode temp = head;
        while (left != null && right != null) {
            if (left.val <= right.val) {
                temp.next=left;
                left = left.next;
                temp = temp.next;
            } else {
                temp.next=right;
                right = right.next;
                temp = temp.next;
            }
        }
        if (left == null) {
            temp.next=right;
        }
        if (right == null) {
            temp.next=left;
        }
        return head;
    }
}