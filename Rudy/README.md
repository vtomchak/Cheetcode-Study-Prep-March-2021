# isPalindrome

```Javascript
function isPalindrome(input) {
    let pointer1 = 0;
    let pointer2 = input.length -1;
    let cleanString = input.replace(/[^0-9a-zA-Z]+/gmi,"")
    while(pointer1 < pointer2) {
        // while pointer1 is space pointer +1
        while(pointer1 < pointer2 && input[pointer1] === " "){
            pointer1++;
        }
        //while pointer2 is space pointer2 --
        while(pointer1 < pointer2 && input[pointer2] === " ") {
            pointer2--;
        }
        if (input[pointer1].toLowerCase() === input[pointer2].toLowerCase()) {
            pointer1++;
            pointer2--;
        } else {
            return false
        }
    }
    return true
}
// Test Cases
input = "R acecar1232 ,,,,,   ****"
console.log(isPalindrome(input))
input2 = "racecagggr"
console.log(isPalindrome(input2))
```

# Container With Most Water

```Javascript
var maxArea = function(height) {
  let pointer1 = 0;
  let pointer2 = height.length-1;
  let maxArea = 0;

  while(pointer1 < pointer2) {
      let currentArea = Math.min(height[pointer1], height[pointer2])*(pointer2-pointer1);
      maxArea = Math.max(currentArea, maxArea)
      if (height[pointer1] < height[pointer2]){
          pointer1++
      } else {
          pointer2--
      }
  }
  return maxArea
};

```
