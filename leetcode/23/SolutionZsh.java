/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class SolutionZsh {
    public ListNode mergeKLists(ListNode[] lists) {

        if (lists == null || lists.length == 0) return null;
        if (lists.length == 1) return lists[0];
        ListNode result = lists[0];
        for (int i = 1; i < lists.length; i++) {
            result = sortAndMerge(result, lists[i]);
        }
        
        return result;
    }

    public ListNode sortAndMerge(ListNode l1, ListNode l2) { 
        ListNode result = new ListNode(0);
        ListNode pre = result;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                pre.next = l1;
                l1 = l1.next;
            } else {
                pre.next = l2;
                l2 = l2.next;
            }
            pre = pre.next;
        }
        pre.next = l1 == null ? l2 : l1;
        return result.next;
    }
}