/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode Merge(ListNode list1,ListNode list2) {
        if (list1 == null || list2 == null) {
            return list1 == null ? list2 : list1;
        }
        ListNode tempNode = new ListNode(0);
        ListNode resultTrue = tempNode;
        // 考点一: 循环时,有一个如果为 null 了,则可以将剩下的链表直接赋值与 result 链表后面,不需要在遍历
        while (list1 != null && list2 != null){
            if (list1.val <= list2.val){
              tempNode.next = list1;
              list1 = list1.next;
            } else {
              tempNode.next = list2;
              list2 = list2.next;
            }
            tempNode = tempNode.next;
        }
        tempNode.next = list1 == null ? list2 : list1;
        return resultTrue.next;
    }
}
