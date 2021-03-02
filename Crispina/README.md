# Question #1 Google Interview Question Two Sum (Easy)

## JavaScript

```
var twoSum = function(nums, target) {
    // create a dictionary
    const dict = new Map();

    // loop through array
    for(let i = 0; i < nums.length; i++) {
        const currentVal = nums[i];
    // subtract one value from main target
        const remainder = target - currentVal;
    // make a check if it's availible
        // if it's a match then
        if(dict.has(remainder)) {
            return [dict.get(remainder) ,i];
        } else {
        // store value as key and index as a value
            dict.set(currentVal, i);
        }
    }
    return -1;
};
```

# Question #2 Container With Most Water (Medium)

```
var maxArea = function(height) {
//the two tallest (biggest integers)
// going through every single pair calulcate thea area
//loop through array
// use a hash map to keep , no need for hash map
// subtraction with the left and right
// area = smallest of (leftValue, rightValue) * (right-left)
let left =0;
let right =height.length-1;
let areaMax =0;

while(left < right){
  areaMax = Math.max(areaMax, Math.min(height[left], height[right]) * (right-left))
  if(height[left]<height[right]){
    left++;
  }
  else {
    right--;
  }
}


return areaMax;
}

console.log(maxArea([1,8,6,2,5,4,8,3,7] )=== 49)

console.log(maxArea([1,1] )=== 1)

console.log(maxArea([4,3,2,1,4] )=== 16)


console.log(maxArea([1,2,1] )=== 2)
```

# Question #3 Trapping Rainwater (Hard)

# Question #4 Backspace String Compare (Easy)

# Question #5 Longest Substring Without Repeating Characters (Medium)

# Question #6a Valid Palindrome(Easy)

# Question #6b Almost Palindrome (Easy)
