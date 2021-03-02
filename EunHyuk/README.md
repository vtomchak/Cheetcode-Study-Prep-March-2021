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
