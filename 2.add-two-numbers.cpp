/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (30.80%)
 * Total Accepted:    808.2K
 * Total Submissions: 2.6M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * Example:
 * 
 * 
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* curr;
        ListNode* res = nullptr;
        int num = 0;
        while(l1&&l2){
            int sum = l1->val + l2->val + num;
            ListNode * node = new ListNode(sum%10);
            num = sum /10;
            if (res){
                curr->next = node;
            }
            else{
                res = node;
            }
            curr = node;
            l1 = l1->next;
            l2 = l2 ->next;
        }
        if (l2){l1 = l2;}
        while (l1){
            int sum = num+ l1 -> val;
            ListNode *node = new ListNode(sum %10);
            num = sum /10;
            curr -> next = node;
            curr = node;
            l1 = l1 -> next;
        }
        if(num){
            ListNode* node = new ListNode(num);
            curr -> next = node;
        }
        return res;

    }
};

