## Question #1 Two Sum (Easy)

```javascript
//nested for-loop solution
var twoSum = function (nums, target) {
  indicesArray = [];
  for (let i = 0; i <= nums.length; i++) {
    for (let j = 0; j <= nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        indicesArray.push(i, j);
        return indicesArray;
      }
    }
  }
};

//hash tables solution
var twoSum = function (nums, target) {
  const hashT = new Map();
  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i];
    if (hashT.has(complement)) {
      return [i, hashT.get(complement)];
    }
    hashT.set(nums[i], i);
  }
};
```

## Question #2 Container With Most Water (Medium)

```javascript
//nested for-loop solution
var maxArea = function (heights) {
  let maxAreaValue = 0;

  for (let i = 0; i < heights.length; i++) {
    for (let j = i + 1; j < heights.length; j++) {
      let height = Math.min(heights[i], heights[j]);
      let width = j - i;
      let area = height * width;
      maxAreaValue = Math.max(maxAreaValue, area);
    }
  }
  return maxAreaValue;
};

//pointer solution
var getMaxWaterContainer = function (heights) {
  let p1 = 0,
    p2 = heights.length - 1,
    maxArea = 0;

  while (p1 < p2) {
    const height = Math.min(heights[p1], heights[p2]);
    const width = p2 - p1;
    const area = height * width;
    maxArea = Math.max(maxArea, area);

    if (heights[p1] <= heights[p2]) {
      p1++;
    } else {
      p2--;
    }
  }
  return maxArea;
};
```

## Question #3 Trapping Rain Water (Hard)



## Question #4 Backspace String Compare (Easy)

```javascript
const buildString = function (string) {
  const builtStringArray = [];
  for (let i = 0; i < string.length; i++) {
    if (string[i] !== "#") {
      builtStringArray.push(string[i]);
    } else {
      builtStringArray.pop();
    }
  }

  return builtStringArray;
};

var backspaceCompare = function (S, T) {
  const finalS = buildString(S);
  const finalT = buildString(T);

  if (finalS.length !== finalT.length) {
    return false;
  } else {
    for (let p = 0; p < finalS.length; p++) {
      if (finalS[p] !== finalT[p]) {
        return false;
      }
    }
  }

  return true;
};
```

## Question #5 Longest Substring Without Repeating Characters(Medium)

```javascript

```

## Question #6a Valid Palindrome (Easy)

```javascript

```

## Question #6b Almost Palindrome (Easy)

```javascript

```
