/**
编写一个程序，找到两个单链表相交的起始节点

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class SolutionZcsh {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p1 = headA;
        ListNode p2 = headB;
        while (p1 != p2) { // 如果相等则退出,哪怕没有节点,都为 null 也算相等
            p1 = p1 == null ? headB : p1.next; // 遍历 a + b
            p2 = p2 == null ? headA : p2.next; // 遍历 b + a 
        }
        return p1;
    }


}