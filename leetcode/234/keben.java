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
        if(head==null||head.next==null){
            return true;
        }
        ListNode p = head,mid=null;
        // 找中点
        ListNode man = head;
        ListNode kuai = head;
        ListNode pre = null;
        while (kuai != null && kuai.next != null) {
            pre = man;
            man = man.next;
            kuai = kuai.next.next;
        }
        if(pre!=null){
            pre.next = null;
        }
        mid = man;
        ListNode revTemp = rev(mid);
        while(revTemp!=null&&p!=null){
            if(revTemp.val!=p.val){
                return false;
            }
            revTemp = revTemp.next;
            p = p.next;
        }
        return true;
    }



    // 倒叙
    public ListNode rev(ListNode head) {
        ListNode temp = head;
        ListNode preNode = null;
        ListNode nextNode = null;
        while (temp != null) {
            nextNode = temp.next;
            temp.next = preNode;
            preNode = temp;
            temp = nextNode;
        }
        return preNode;
    }
}
