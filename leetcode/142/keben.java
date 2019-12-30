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
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode man = head;
        ListNode kuai = null;
        while (man != kuai) {
            if(kuai==null){
                kuai=head;
            }
            if (man == null || kuai == null || kuai.next == null) {
                return null;
            }
            man = man.next;
            kuai = kuai.next.next;
        }
        if(kuai==null){
            return null;
        }
        ListNode temp = head;
        while(kuai!=temp){
            kuai = kuai.next;
            temp = temp.next;
        }
        return kuai;

    }
}
