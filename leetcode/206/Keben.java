package Solution148;

/**
 * @author Keben
 * @description 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
 * 1.归并排序
 * 2.找出一个链表的中间节点
 * 3.合并
 * @date 2019-12-11 09:13
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        // 找到最后一个节点
        // 中
        ListNode mid = head;

        ListNode midPre = null;
        // 尾
        ListNode tail = head;

        // 每次尾巴走两步,mid走一步,  例  (1,3,5,7,9)   这样即求出中点和尾巴
        while (tail != null && tail.next != null) {
            midPre = mid;
            mid = mid.next;
            tail = tail.next.next;
        }
        midPre.next=null;
        // 左
        ListNode left = sortList(head);
        // 中
        ListNode right = sortList(mid);
        // 1.先拆分
        return merge(left, right);
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
