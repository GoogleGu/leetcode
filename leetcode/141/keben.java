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
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        ListNode man = head;
        ListNode kuai = head.next;
        while (man != kuai) {
            if (man == null || kuai == null || kuai.next == null) {
                return false;
            }
            man = man.next;
            kuai = kuai.next.next;
        }
        return true;
    }
}
