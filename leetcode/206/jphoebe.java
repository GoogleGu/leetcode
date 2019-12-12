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
    public ListNode reverseList(ListNode head) {
        if (head.next != null){
            reverseList(head.next);
        }
        if (listNode == null){
            listNode = new ListNode(head.val);
        } else{
            listNode.next = new ListNode(head.val);
        }
        return listNode;
    }

    public ListNode reverseList2(ListNode head) {
        ListNode current, preview = head;
        head = head.next;
        while (head != null){
            ListNode nextTemp = head.next;
            current = head;
            current.next = preview;
            preview = current;
            head = nextTemp;
        }
        return head;
    }

}
