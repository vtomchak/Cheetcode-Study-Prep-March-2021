# Clean Code Handbook
## Table of contents

1. [Two Sum](#Two-Sum)
1. [Two Sum II-- Input Array Sorted](#Two-Sum-II---Input-Array-Sorted)
2. [Two Sum III – Data structure design](#Two-Sum-III-–-Data-structure-design)
2. [Longest Substring Without Repeating Characters](#longest-substring-without-repeating-characters)
3. [Valid Palindrome](#Valid-Palindrome)
4. [Merge Two Sorted Lists](#Merge-Two-Sorted-Lists)
5. [Swap Nodes in Pairs](#Swap-Nodes-in-Pairs)
6. [Merge K Sorted Linked Lists](#Merge-K-Sorted-Linked-Lists)
7. [Copy List with Random Pointer](#Copy-List-with-Random-Pointer)

## Two Sum
```javascript
find(arr, target){
  let hashMap = {}
  for(let i = 0; i < arr.length; i ++ ){
    let currNum = arr.val[i]
    let numToFind = target - currNum
      hashMap[currNum] = i
    if(hashMap[numToFind] !== undefined){
      return true
    }
  }
  return false
}
```
## Two Sum II-- Input Array Sorted
```javascript
const twoSumTwo = function(arr, target) {
    let p1 = 0;
    let p2 = arr.length - 1;
    while (p1 < p2) {
        if (arr[p1] + arr[p2] == target)
            return [p1, p2];
        else if (arr[p1] + arr[p2] > target)
            p2--;
        else
            p1++;
    }
};
```
## Two Sum III – Data structure design
```javascript
class TwoSum {
  constructor(val){
  this.val = []
  }
addItem(item){
  return this.val.push(item)
}

find(target){
  let hashMap = {}
  for(let i = 0; i < this.val.length; i ++ ){
    let currNum = this.val[i]
    let numToFind = target - currNum
      hashMap[currNum] = i
    if(hashMap[numToFind] !== undefined){
      return true
    }
  }
  return false
}

}

// let test = new TwoSum()
// test.addItem(1)
// test.addItem(2)
// test.addItem(2)
// console.log(test.find(4))
```
## Longest Substring Without Repeating Characters
```javascript
const LongestSubstringWithoutRepeat = function(str) {
    if(str.length <= 1) return str.length;
    const seen = {};
    // hashmap for storing previously seen values and their indices
    let pointer1 = 0
    let longest = 0;
    // start left pointer1 at position 0 and initialize longest seen varible as 0
    for(let pointer2 = 0; pointer2 < str.length; pointer2++) {
        const currChar = str[pointer2];
        const prevSeenChar = seen[currChar];
        if(prevSeenChar >= pointer1) {
        // if a character has been seen but is before where pointer 1 is pointing it does not need to be counted as seen
          pointer1 = prevSeenChar + 1;
        }
        seen[currChar] = pointer2;
        longest = Math.max(longest, pointer2 - pointer1 + 1);
    }
    return longest;
};
```
## Valid Palindrome
Two pointers from outside
```javascript
const isValidPalindrome = function(s) {
    s = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
    // initialize left/right pointers at start and end of string respectively
    let left = 0; right = s.length - 1;
    // loop through string characters while comparing them, then move the pointers closer to the center
    while(left < right) {
        if(s[left] !== s[right]) {
            return false
        }
        left++;
        right--;
    }
    return true;
};

function validPal(str) {
  str = str.replace(/[^a-z0-9+]+/gi, '').toLowerCase()
  let pointer1 = 0
  let pointer2 = str.length-1
  while(pointer1 < pointer2){
    pointer1++
    pointer2--
    if(str[pointer1] !== str[pointer2]){
      return false
    }
  }
  return true
}
```
## Implement strstr()
```javascript

```
## Merge Two Sorted Lists
## Add Two Numbers
## Swap Nodes in Pairs
## Merge K Sorted Linked Lists
## Copy List with Random Pointer
