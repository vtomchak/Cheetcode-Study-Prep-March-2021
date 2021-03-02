## Question #1 Two Sum (Easy)

```javascript
//nested for-loop solution
var twoSum = function(nums, target) {
   indicesArray = []
   for(let i = 0; i <= nums.length; i++) {
      for(let j = 0; j <=nums.length; j++) {
         if(nums[i] + nums[j] === target) {
            indicesArray.push(i, j)
            return indicesArray
         }
      }
   }
}

//hash tables solution
var twoSum = function(nums, target) {
   const hashT = new Map()
   for(let i = 0; i < nums.length; i++) {
      let complement = target - nums[i]
      if(hashT.has(complement)) {
         return [i, hashT.get(complement)]
      }
      hashT.set(nums[i], i)
   }
}
