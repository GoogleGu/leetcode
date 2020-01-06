/**
 * Definition for singly-linked list.
 *     1-2
 *     3
 *
 *    第一次  1 3
 *    第二次  2 null
 *    第三次  null 1
 *    第四次  3 2
 *    第五次  null null
 *
 *    5-1-2-3
 *    4-2
 *    第一次 5 4
 *    第二次 1 2
 *    第三次 2 null
 *    第四次 3 5
 *    第五次 null 1
 *    第六次 4 2
 *    第七次 2 3
 *    第八次 null null
 *
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA==null||headB==null){
            return null;
        }
        ListNode a=  headA;
        ListNode b = headB;
        while (a!=b){
            if (a==null){
                a= headB;
            }else {
                a=a.next;
            }
            if (b==null){
                b= headA;
            }else {
                b=b.next;
            }
        }

        return a;

    }
}