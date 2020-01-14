/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode newNode = new ListNode(-1);
        newNode.next = head;
        ListNode fastNode = newNode;
        ListNode slowNode = newNode;
        for (int i=0;i<=n;i++){
            fastNode =fastNode.next;
        }
        while (fastNode!=null){
            fastNode=fastNode.next;
            slowNode=slowNode.next;
        }
        slowNode.next =slowNode.next.next;
        return newNode.next;
    }
}