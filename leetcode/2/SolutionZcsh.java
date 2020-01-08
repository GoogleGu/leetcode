/**
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class SolutionZcsh {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        boolean isCarry = false;

        ListNode result = new ListNode(0);
        ListNode parent = result;
        while (l1 != null || l2 != null) {
            int val = 0;
            if (l1 != null) {
                val += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                val += l2.val;
                l2 = l2.next;
            }
            // 是否需要进位
            if (isCarry) {
                val++;
                isCarry = false;
            }
            // 如果大于 10 则需要进位
            if (val >= 10) {
                val = val % 10;
                isCarry = true;
            }

            parent.next = new ListNode(val);
            parent = parent.next;
        }

        // 如果在最后一个节点相加后,也需要进位,则在最后加一个节点
        if (isCarry) parent.next = new ListNode(1);
        return result.next;
    }


}