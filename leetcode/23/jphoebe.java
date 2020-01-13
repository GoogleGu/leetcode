/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {

        if (lists == null || lists.length == 0){
            return null;
        } else if(lists.length == 1){
            return lists[0];
        }
        ListNode result = this.mergeTwoLists(lists[0], lists[1]);
        if(lists.length == 2){
            return result;
        }
        for (int i = 2; i < lists.length; i++) {
            result = this.mergeTwoLists(result, lists[i]);
        }
        return result;
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null || l2 == null) {
            return l2 == null ? l1 : l2;
        }
        ListNode temp = l1;
        if (l1.val > l2.val) {
            l1 = l2;
            l2 = temp;
        }
        ListNode start = l1;
        ListNode temp1_pre = l1;
        while (l1 != null && l2 != null) {
            if (l1.val > l2.val) {
                temp1_pre.next = l2;
                temp = l2.next;
                l2.next = l1;
                temp1_pre = l2;
                l2 = temp;
            } else {
                temp1_pre = l1;
                l1 = l1.next;
            }
        }
        if (l2 != null) {
            temp1_pre.next = l2;
        }
        return start;
    }
}
