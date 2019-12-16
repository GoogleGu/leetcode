/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class SolutionZcsh {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode right = slow.next;
        slow.next = null;
        ListNode left = sortList(head);
        right = sortList(right);

        ListNode result = new ListNode(0);
        result.next = left;
        ListNode item = result;
        while (left != null && right != null) {
            if (left.val < right.val) {
                left = left.next;
            } else {
                item.next = right;
                right = right.next;
                item.next.next = left;
            }
            item = item.next;
        }

        item.next = left == null ? right : left;
        return result.next;

    }
    
}
