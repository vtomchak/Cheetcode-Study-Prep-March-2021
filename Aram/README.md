## Question #1 Google Interview Question Two Sum (Easy)

```JavaScript

function twoSum(nums, target) {
    if (nums.length < 2) return nums
    let storage = []
    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i]
        if (nums.includes(diff) === true) {
            storage = [i, nums.indexOf(diff)]
        }
    } return storage
}

```

## Question #2 Container With Most Water (Medium)

```JavaScript

function maxArea(heights) {
    let maxOne = 0
    let maxTwo = heights.length - 1
    let maxArea = 0

    while (maxOne < maxTwo) {
        const width = maxTwo - maxOne
        const height = Math.min(heights[maxOne], heights[maxTwo])
        const area = width * height
        const maxArea = Math.max(maxArea, area)
        
        if (heights[maxOne] <= heights[maxTwo]) {
            maxOne++
        } else {
            maxTwo++
        }
    }
    return maxArea
}

```

## Question # 3 Trapping Rain Water (Hard)

```JavaScript

function trap(heights) {
    let maxArea = 0
    let maxHeight = 0
    let current = i - 1
    let next = i + 1

    while (heights[current] === null && heights[next] === null) {
        const currentHeight = Math.max(heights[current], heights[next])
        const maxHeight = Math.max(currentHeight, maxHeight)
        if (heights[current] - heights[next] > 0) {
            const diff = maxHeight - heights[next]
            maxArea += diff
            current++, next++
        } 
        else {
            current++, next++
        }  
    } return maxArea 
}

```

## Question #4 Backspace String Compare (Easy)

```JavaScript

function backSpaceCompare(S, T) {
    let s = []
    let t = []

    for (let i = 0; i < S.length; i++) {
        if (S[i] === '#') {
            s.pop()
        } else {
            s.push(S[i])
        }
    }
    for (let i = 0; i < T.length; i++) {
        if (T[i] === '#') {
            t.pop()
        } else {
            t.push(T[i])
        }
    }
    s = s.join('')
    t = t.join('')
    return s === t
}

```

## Question #5 Longest Substring Without Repeating Characters (Medium)

```JavaScript

function substringCheck(s) {
    const memo = {}
    let longest = [0, 1]
    let start = 0

    for (let i = 0; i < s.length; i++) {
        const letter = s[i]
        if (letter in memo) {
            start = Math.max(start, memo[letter] + 1)
        }
        if (longest[1] - longest[0] < i + 1 - start) {
            longest = [start, i + 1]
        }
        memo[letter] = i
    } return s.slice(longest[0], longest[1])
}

```

## Question #6a Valid Palindrome (Easy) 

```JavaScript

function palindromeCheck(s) {
    leftIndex = 0
	rightIndex = string.length - 1
	
    while(leftIndex < rightIndex) {
        leftLetter = s[leftIndex].toLowerCase()
        rightLetter = s[rightIndex].toLowerCase()
        
        if (leftLetter !== rightLetter) return false
        leftIndex++
        rightIndex++
    }
    return true
}

```

## Question #6b Almost Palindrome (Easy) 

```JavaScript

function validPalindrome(s) {
     let start = 0;
  let end = s.length - 1;
  while (start < end) {
      if (s[start] !== s[end]) {
          return validSubPalindrome(s, start + 1, end) || validSubPalindrome(s, start, end - 1);
      }
      start++;
      end--;
  }
  return true;
};

const validSubPalindrome = function(s, start, end) {
  while (start < end) {
      if (s[start] !== s[end]) {
          return false;
      }
      start++;
      end--;
  }
  return true;
}

```




