## Question #1 Google Interview Question Two Sum (Easy)

```javascript
var twoSum = function (nums, target) {
  let hashTable = {};

  for (let [index, num] of nums.entries()) {
    if (hashTable[num] !== undefined) return [hashTable[num], index];
    hashTable[target - num] = index;
  }
};
```
