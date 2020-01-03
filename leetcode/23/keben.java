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
        ListNode temp = null;
        for(int i = 0;i<lists.length;i++){
            if(temp==null){
                temp = lists[i];
                i++;
            }
            if(i>=lists.length){
                break;
            }
            temp = merge(temp,lists[i]);
        }
        return temp;
    }

    public ListNode merge(ListNode left, ListNode right) {
        ListNode temp = new ListNode(-1);
        // 当前节点
        ListNode curr = temp;

        while (left != null && right != null) {
            if (left.val <= right.val) {
                curr.next = left;
                curr = curr.next;
                left = left.next;
            } else {
                curr.next = right;
                curr = curr.next;
                right = right.next;
            }
        }
        if (left != null) {
            curr.next = left;
        }
        if (right != null) {
            curr.next = right;
        }
        return temp.next;
    }
}
