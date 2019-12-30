
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
        ListNode newHead = hebing(head, fast); 1 4
        return newHead;
    }


    public ListNode hebing(ListNode left, ListNode right) {
        ListNode head;
        if (left.val<= right.val) {
            head = left; 3 2 1
            left = left.next; 21
        } else {
            head = right;
            right = right.next;
        }
        ListNode temp = head; 3 2 1
        while (left != null && right != null) {
                2 1          4
            if (left.val <= right.val) {
                temp.next=left; 2 1      1
                left = left.next; 1      null
                temp = temp.next;  21    1
            } else {
                temp.next=right;
                right = right.next;
                temp = temp.next;
            }
        }
        if (left == null) {
            temp.next=right;   4
        }
        if (right == null) {
            temp.next=left;
        }
         // temp 1 4
        return head;
    }
}