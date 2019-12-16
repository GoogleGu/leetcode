/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class SolutionZcsh {
    // public ListNode reverseList(ListNode head) {
    //     ListNode result = null;
    //     while (head != null){
    //         ListNode temp = head.next;
    //         head.next = result;
    //         result = head;
    //         head = temp;
    //     } 
    //     return result;
    // }

    public ListNode reverseList(ListNode head) {
        return reverse(null, head);
    }
    public ListNode reverse(ListNode pre, ListNode current) {
        if (current == null) return pre;
        ListNode temp = current.next;
        current.next = pre;
        return reverse(current, temp);
    }
}
