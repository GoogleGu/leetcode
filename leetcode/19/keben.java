/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public static ListNode removeNthFromEnd(ListNode head, int n) {
        // 1. 两个节点. 一个 每次走一格子
        // 2. 一个每次走n点
        ListNode man = head, kuai = head, manPre = null;
        int index = 0, kuaiIndex = 0;
        boolean isEnd = false;
        while (man != null) {
            for (int i = n; i > 0 && kuai != null; i--) {
                if (kuai.next == null) {
                    isEnd = true;
                }
                kuai = kuai.next;
                kuaiIndex++;
            }

            if (isEnd && index == (kuaiIndex - n)) {
                if (manPre == null) {
                    return man.next;
                }
                manPre.next = man.next;
                break;
            }

            manPre = man;
            man = man.next;
            index++;
        }
        return head;
    }

}
