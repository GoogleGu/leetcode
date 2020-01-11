/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null){
            return true;
        }
        ListNode fast = head, slow = head;
        if (fast.next != null){
            fast = fast.next;
        }
        // 找到重点
        while (fast != null){
            if (fast.next != null){
                fast = fast.next.next;
                slow = slow.next;
            }else{
                fast = fast.next;
            }
        }

        // 倒叙
        ListNode pre = null, current = null;
        while (slow != null){
            current = slow.next;
            slow.next = pre;
            pre = slow;
            slow = current;
        }
        // 比较
        while (head!=null && pre!=null){
            if (head.val != pre.val){
                return false;
            }
            head = head.next;
            pre = pre.next;
        }
        return true;
    }
}
