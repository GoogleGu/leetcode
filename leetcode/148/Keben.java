class Solution {
        public ListNode reverseList(ListNode head) {
        return recursion(head);
    }

    public ListNode iterator(ListNode head) {
        ListNode preNode = null;
        ListNode nextNode = null;
        while (head != null) {
            nextNode = head.next;
            head.next = preNode;
            preNode = head;
            head = nextNode;
        }
        return preNode;
    }



    public ListNode recursion(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode newHead = recursion(head.next);
        head.next.next=head;
        head.next = null;
        return newHead;
    }
}
