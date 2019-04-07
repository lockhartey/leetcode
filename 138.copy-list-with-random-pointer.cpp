/*
 * @lc app=leetcode id=138 lang=cpp
 *
 * [138] Copy List with Random Pointer
 *
 * https://leetcode.com/problems/copy-list-with-random-pointer/description/
 *
 * algorithms
 * Medium (26.20%)
 * Total Accepted:    231.6K
 * Total Submissions: 883.4K
 * Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
 *
 * A linked list is given such that each node contains an additional random
 * pointer which could point to any node in the list or null.
 * 
 * Return a deep copy of the list.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input:
 * 
 * {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
 * 
 * Explanation:
 * Node 1's value is 1, both of its next and random pointer points to Node 2.
 * Node 2's value is 2, its next pointer points to null and its random pointer
 * points to itself.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * You must return the copy of the given head as a reference to the cloned
 * list.
 * 
 */
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
// Consider l1 as a node on the 1st list and l2 as the corresponding node on 2nd list.
// Step 1:
// Build the 2nd list by creating a new node for each node in 1st list. 
// While doing so, insert each new node after it's corresponding node in the 1st list.
// Step 2:
// The new head is the 2nd node as that was the first inserted node.
// Step 3:
// Fix the random pointers in the 2nd list: (Remember that l1->next is actually l2)
// l2->random will be the node in 2nd list that corresponds l1->random, 
// which is next node of l1->random.
// Step 4:
// Separate the combined list into 2: Splice out nodes that are part of second list. 
// Return the new head that we saved in step 2.
//
class Solution {
public:
    Node *copyRandomList(Node *head) {  
        if(head ==NULL) return NULL;
        Node* result;
        if(m.find(head->val) == m.end()){
            result = new Node(head->val);
            m.emplace(pair(result->val,result));

            result->random = copyRandomList(head->random);
            result->next = copyRandomList(head->next);
        }
        else{
            result = m[head->val];
        }
        return result;
    }
private:
    map<int, Node*> m;
};

