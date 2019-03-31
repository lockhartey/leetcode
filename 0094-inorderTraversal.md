#Describe
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

## Method 0
### Recursive
* In the order of  left --> root --> right, in-placely maintain a vector to store the output.

```cpp
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
    vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> v;
        std::inorderTraversal(TreeNode* root,v);
        inorderTraversal(root,v);
        return v;
    }

    void inorderTraversal(TreeNode *root,std::vector<int> &v)
    {
        if (root==NULL)return;
        inorderTraversal(root->left,v);
        v.push_back(root->val);
        inorderTraversal(root->right,v);
    }
};
```

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> v;
        std::inorderTraversal(TreeNode* root,v);
        inorderTraversal(root,v);
        return v;
    }
    void inorderTraversal(TreeNode* root,std::vector<int> &v)
    {
        if (root == NULL) return;
        inorderTraversal(root->left,v);
        v.push_back(root->val);
        inorderTraversal(root->right,v);
    }
};

