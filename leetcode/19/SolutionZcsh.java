/**
 * 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode result = head;
        ListNode deleteParentNode = head;
        while (head != null) {
            if (n < 0) deleteParentNode = deleteParentNode.next;
            head = head.next;
            n--;
            
        }
        if (n == 0) return result.next;  // 头节点就是要删除的节点
        if (n < 0) deleteParentNode.next = deleteParentNode.next.next;
        return result;
    }
}