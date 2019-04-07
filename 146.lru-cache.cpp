/*
 * @lc app=leetcode id=146 lang=cpp
 *
 * [146] LRU Cache
 *
 * https://leetcode.com/problems/lru-cache/description/
 *
 * algorithms
 * Hard (24.52%)
 * Total Accepted:    274.6K
 * Total Submissions: 1.1M
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * 
 * Design and implement a data structure for Least Recently Used (LRU) cache.
 * It should support the following operations: get and put.
 * 
 * 
 * 
 * get(key) - Get the value (will always be positive) of the key if the key
 * exists in the cache, otherwise return -1.
 * put(key, value) - Set or insert the value if the key is not already present.
 * When the cache reached its capacity, it should invalidate the least recently
 * used item before inserting a new item.
 * 
 * 
 * Follow up:
 * Could you do both operations in O(1) time complexity?
 * 
 * Example:
 * 
 * LRUCache cache = new LRUCache( 2 /* capacity  );
 * 
 * cache.put(1, 1);
 * cache.put(2, 2);
 * cache.get(1);       // returns 1
 * cache.put(3, 3);    // evicts key 2
 * cache.get(2);       // returns -1 (not found)
 * cache.put(4, 4);    // evicts key 1
 * cache.get(1);       // returns -1 (not found)
 * cache.get(3);       // returns 3
 * cache.get(4);       // returns 4
 * 
 * 
 */
#include<unordered_map>
#include<list>
using namespace std;

class LRUCache {
private:
    int capacity;
    list<pair<int,int>> m_list;//contain the order information 
    unordered_map<int,list<pair<int,int>>::iterator>m_map;//contain the information of elements
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        auto found_iter = m_map.find(key);
        if(found_iter==m_map.end()) return -1;
        m_list.splice(m_list.begin(),m_list,found_iter->second);
        return found_iter->second->second;
    }
    
    void put(int key, int value) {
        auto found_iter = m_map.find(key);
        if(found_iter != m_map.end()){//key exists
            m_list.splice(m_list.begin(),m_list,found_iter->second);
            found_iter->second->second = value;
            return;
        }
        if(m_map.size() == capacity){
            int key_to_del = m_list.back().first;
            m_list.pop_back();
            m_map.erase(key_to_del);
        }
        m_list.emplace_front(key,value);
        m_map[key] = m_list.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

