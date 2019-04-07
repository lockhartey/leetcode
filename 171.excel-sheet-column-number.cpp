/*
 * @lc app=leetcode id=171 lang=cpp
 *
 * [171] Excel Sheet Column Number
 *
 * https://leetcode.com/problems/excel-sheet-column-number/description/
 *
 * algorithms
 * Easy (51.07%)
 * Total Accepted:    212.5K
 * Total Submissions: 415.7K
 * Testcase Example:  '"A"'
 *
 * Given a column title as appear in an Excel sheet, return its corresponding
 * column number.
 * 
 * For example:
 * 
 * 
 * ⁠   A -> 1
 * ⁠   B -> 2
 * ⁠   C -> 3
 * ⁠   ...
 * ⁠   Z -> 26
 * ⁠   AA -> 27
 * ⁠   AB -> 28 
 * ⁠   ...
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "A"
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "AB"
 * Output: 28
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "ZY"
 * Output: 701
 * 
 */
using namespace std;
#include<string>
#include<math.h>
class Solution {
public:
    int titleToNumber(string s) {
        if(s.empty()) return 0;
        int num = 0;
        int bit = 0;
        for(int i=s.size()-1;i>=0;i--){
            num = num + (s[i]-64)*pow(26,bit);
            bit ++;
        }
        return num;
    }
};

