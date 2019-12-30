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
        List list = new ArrayList();
        while (head!=null){
            if (list.contains(head)){
                return head;
            }else {
                list.add(head);
            }
            head = head.next;
        }
        return null;
    }
}