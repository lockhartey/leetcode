/*
 * @lc app=leetcode id=151 lang=cpp
 *
 * [151] Reverse Words in a String
 *
 * https://leetcode.com/problems/reverse-words-in-a-string/description/
 *
 * algorithms
 * Medium (16.19%)
 * Total Accepted:    267.7K
 * Total Submissions: 1.6M
 * Testcase Example:  '"the sky is blue"'
 *
 * Given an input string, reverse the string word by word.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "the sky is blue"
 * Output: "blue is sky the"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "  hello world!  "
 * Output: "world! hello"
 * Explanation: Your reversed string should not contain leading or trailing
 * spaces.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "a good   example"
 * Output: "example good a"
 * Explanation: You need to reduce multiple spaces between two words to a
 * single space in the reversed string.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * A word is defined as a sequence of non-space characters.
 * Input string may contain leading or trailing spaces. However, your reversed
 * string should not contain leading or trailing spaces.
 * You need to reduce multiple spaces between two words to a single space in
 * the reversed string.
 * 
 * 
 * 
 * 
 * Follow up:
 * 
 * For C programmers, try to solve it in-place in O(1) extra space.
 */
#include<string>
#include<iostream>
#include<stack>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        stack<string> stk;
        int len = s.length();
        int pos = 0;
        string res;
        while(pos<len){
            int start,end;
            while(s[pos]==' '&&pos<len) pos++;
            start = pos;
            while(s[pos]!=' '&&pos<len) pos++;
            end = pos;

            if(start == end) break;
            stk.push(s.substr(start,end-start));
        }

        while(!stk.empty()){
            res+= stk.top()+" ";
            stk.pop();
            // if(!stk.pop)

        }
        return res.substr(0,res.length()-1);
    }
};

