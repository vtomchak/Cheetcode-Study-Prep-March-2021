##Question #1 Google Interview Question Two Sum (Easy)

```Javascript
var twoSum = function (nums, target) {
  let memo = {};
  for (let i = 0; i < nums.length; i++) {
    let val = target - nums[i];
    if (nums[i] in memo) {
      return [i, nums[i]];
    } else {
      memo[val] = i;
    }
  }
};

//Time: O(n) Space: O(1)
//Linear Time Complexity & constant space
```

## Question #2 Container With Most Water (Medium)

```Javascript
var maxArea = function (height) {
  let maxArea = 0;
  let pointer1 = 0;
  let pointer2 = height.length - 1;
  while (pointer2 > pointer1) {
    let length = Math.min(height[pointer1], height[pointer2]);
    let width = pointer2 - pointer1;
    let area = length * width;
    maxArea = Math.max(maxArea, area);
    //checking to see which value is greater and shifts the pointers based on condition
    if (height[pointer1] <= height[pointer2]) {
      pointer1++;
    } else {
      pointer2--;
    }
  }
  return maxArea;
};

//Time: O(n)
//Space: O(1)

```

## Question #3 Trapping Rainwater (Hard)

```Javascript
//Todo:
```

## Question #4 Backspace String Compare (Easy)

```Javascript
var backspaceCompare = function (S, T) {
  let sArr = [];
  let tArr = [];
  for (let i = 0; i < S.length; i++) {
    if (S[i] === "#") {
      sArr.pop();
    } else {
      sArr.push(S[i]);
    }
  }
  for (let j = 0; j < T.length; j++) {
    if (T[j] === "#") {
      tArr.pop();
    } else {
      tArr.push(T[j]);
    }
  }
  sArr = sArr.toString();
  tArr = tArr.toString();

  return sArr === tArr;
};

//Time: O(n) Space: O(n)
```

## Question #5 Longest Substring Without Repeating Characters (Medium)

```Javascript

```

## Question #6a Valid Palindrome(Easy)

```Javascript
var isPalindrome = function (s) {
  let lowerCaseStr = s.toLowerCase();
  let left = 0;
  let right = lowerCaseStr.length - 1;
  while (left < right) {
    if (lowerCaseStr[left] !== lowerCaseStr[right]) {
      return false;
    } else {
      left++;
      right--;
    }
  }
  return true;
};

//Todo: go over regex and how to remove spaces from a string
```
