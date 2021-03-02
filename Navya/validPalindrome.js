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
