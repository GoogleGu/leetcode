/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class SolutionZcsh {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;
        if (head.next.next == head) return head;
        ListNode fast = head.next.next;
        ListNode slow = head.next;
        while (fast != null && fast.next != null && fast != slow) {
            fast = fast.next.next;
            slow = slow.next;
        }
        if (fast == null || fast.next == null) return null;
        ListNode innerRing = slow;
        ListNode newHead = head;
        while (newHead != innerRing) {
            innerRing = innerRing.next;
            newHead = newHead.next;
        }
        return innerRing;
    }
}
