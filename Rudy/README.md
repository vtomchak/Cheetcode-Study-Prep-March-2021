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

# Trapping Rain Water

```Javascript
const trap = function(height) {
  let l = 0;
  let r = height.length - 1;
  let lowPoint = 0;
  let result = 0;
  while (l < r) {
    const lval = height[l];
    const rval = height[r];
    if (lval > lowPoint && rval > lowPoint) {
      lowPoint = Math.min(lval, rval);
    }
    if (lval <= lowPoint) {
      result += lowPoint - lval;
      l += 1;
      continue;
    }
    if (rval <= lowPoint) {
      result += lowPoint - rval;
      r -= 1;
    }
  }
  return result;
};

```

# Backspace String Compare

```Javascript

function editProcess (string) {
    const result = [];
    for (char of string.split('')) {
        //.pop removes last element of the array
        char === '#' ? result.pop() : result.push(char)
    }
    return result.join('')
}

function backspaceCompare(S,T) {
    return editProcess(S) == editProcess(T)
}

```

#Backspace String Compare 2-Pointer

```Javascript
var backspaceCompare = function(S, T) {
    let s=S.length-1;
    let t=T.length-1;

    const handleSkip = (U, u) => {
        let count = 0;
        while (U[u]==='#'){
            do {
                if (U[u]==='#'){
                    count++;
                }else{
                    count--;
                }
                u--;
            }while (count > 0)
        }
        return u;
    }

    while (s>=0&&t>=0){
        s = handleSkip(S,s);
        t = handleSkip(T,t);
        if (S[s]!==T[t]) return false;
        s--;
        t--;
    }
    // one end and another hasn't
    if (s>=0){
        s = handleSkip(S,s);
    }
    if (t>=0){
        t = handleSkip(T,t);
    }
    return s<0 && t <0;
```
