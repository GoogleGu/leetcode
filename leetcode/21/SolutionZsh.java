class SolutionZsh {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode parent = result;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                parent.next = l1;
                l1 = l1.next;
            } else {
                parent.next = l2;
                l2 = l2.next;
            }
            parent = parent.next;
        }

        parent.next = l1 == null ? l2 : l1;
        return result.next;
    }
}