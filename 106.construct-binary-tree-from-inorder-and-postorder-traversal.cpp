/*
 * @lc app=leetcode id=106 lang=cpp
 *
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (38.41%)
 * Total Accepted:    145.2K
 * Total Submissions: 377.9K
 * Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
 *
 * Given inorder and postorder traversal of a tree, construct the binary tree.
 * 
 * Note:
 * You may assume that duplicates do not exist in the tree.
 * 
 * For example, given
 * 
 * 
 * inorder = [9,3,15,20,7]
 * postorder = [9,15,7,20,3]
 * 
 * Return the following binary tree:
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return dfs(inorder,postorder,0,inorder.size()-1,0,postorder.size()-1);
    }
    TreeNode* dfs(vector<int> & inorder,vector<int>& postorder,int is,int ie,int ps,int pe){
        if(ps>pe) return nullptr;
        TreeNode* node = new TreeNode(postorder[pe]);
        int pos;
        for(int i = is;i<=ie;i++){
            if(inorder[i] == node->val){
                pos = i;
                break;
            }
        }
        node -> left = dfs(inorder,postorder,is,pos-1,ps,ps+pos-is-1);
        node -> right = dfs(inorder,postorder,pos+1,ie,pe-ie+pos,pe-1);
        return node;
        }
};

