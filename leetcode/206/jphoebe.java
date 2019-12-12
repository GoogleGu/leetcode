package com.yunlsp.pay.sdktest.controller;


class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {

    ListNode listNode;
    ListNode newHead = null;
    public ListNode reverseList(ListNode head) {
        if (head != null){
            if (head.next != null){
                reverseList(head.next);
            }
            if (listNode == null){
                listNode = new ListNode(head.val);
                newHead = listNode;
            } else{
                listNode.next = new ListNode(head.val);
                listNode = listNode.next;
            }
        }
        return newHead;
    }

    public ListNode reverseList2(ListNode head) {
        ListNode current = head.next, preview = head;
//        ListNode current = head, preview = null;
        while (current != null){
            ListNode temp = current.next;
            current.next = preview;
            preview = current;
            current = temp;
        }
      

}
