
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
public class Solution {

    public ListNode EntryNodeOfLoop(ListNode pHead) {
        if (pHead == null) {
            return null;
        }
        // 是否有环
        ListNode p1 = pHead, p2 = pHead;
        // 环最少有两个节点
        boolean isCircular = false;
        while (p2.next != null && p2.next.next != null) {
            p1 = p1.next;
            p2 = p2.next.next;
            if (p1 == p2) {
                isCircular = true;
                break;
            }
        }
        if (!isCircular) {
            return null;
        }

        // p1 和 p2 重合，任何一个点走一圈就是圆周长
        int length = 1;
        p2 = p2.next;
        while (p1 != p2) {
            ++length;
            p2 = p2.next;
        }

        // 从头开始，p2先走一圈，重逢的时候就是入口
        p1 = pHead;
        p2 = pHead;
        for (int i = 0; i < length; i++) {
            p2 = p2.next;
        }
        while (p1 != p2) {
            p1 = p1.next;
            p2 = p2.next;
        }
        return p1;
    }
}
