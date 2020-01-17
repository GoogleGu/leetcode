/**
请判断一个链表是否为回文链表

 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class SolutionZcsh {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true; // [] 和 只有 1 个值,也是回文
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode middle = slow;
        if (fast != null) {
            middle = slow.next;
            slow.next = null;
        }

        ListNode right = reversal(middle);
        
        while (head != null && right != null && head.val == right.val) {
            head = head.next;
            right = right.next;
        } 

        return head == right;
    }

    public ListNode reversal(ListNode listNode) {
        ListNode pre = null;
        while (listNode != null) {
            ListNode temp = listNode.next;
            listNode.next = pre;
            pre = listNode;
            listNode = temp;
        }
        return pre;
    }
}