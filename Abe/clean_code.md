### Valid Palindrome
```python
def is_palindrome(s: str) -> bool:
    """Check if string is palindrome."""
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True
```

### Valid Palindrome II   

Create a recursive function.
recurse(string, left, right, deleted):
    check if string[left] != string[right] 
        if we already did a delete return false
        else we left+ 1 or right +1 with deleted = True


```python
class Solution(object):
    def validPalindrome(self, s):
        def verify(s, left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return verify(s, left + 1, right, True) or verify(s, left, right - 1, True)
                else:
                    left += 1
                    right -= 1
            return True

        return verify(s, 0, len(s) - 1, False)
```

### Kth Largest Element in an Array
```python
import heapq 

def template(mylist, k):
    """Given a list of elements returns the klargest"""
    heap = []

    for element in mylist:
        if len(heap) < k:
            heapq.heappush(heap, element)

        else:
            if element > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, element)

    return heap[0]
```

### Serialize and Deserialize Binary Tree
```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return []
        encoded_tree = []

        myqueue = deque()
        myqueue.append(root)

        while myqueue:
            current = myqueue.popleft()

            if current:
                encoded_tree.append(current.val)
                myqueue.append(current.left)
                myqueue.append(current.right)
            else:
                encoded_tree.append(None)

        return encoded_tree

    def deserialize(self, data):
        if not data:
            return []

        root = TreeNode(data[0])
        myqueue = deque([root])
        i = 1
        while myqueue:
            current_node = myqueue.popleft()

            if data[i] is not None:
                current_node.left = TreeNode(data[i])
                myqueue.append(current_node.left)
            i += 1

            if data[i] is not None:
                current_node.right = TreeNode(data[i])
                myqueue.append(current_node.right)
            i += 1

        return root
```

### Add Binary   
```python
def addBinary(a, b) -> str:
    """Add two binary strings"""
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)

    carry = 0
    answer = []
    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1

        if carry % 2 == 1:
            answer.append('1')
        elif carry % 2 == 0:
            answer.append('0')

        carry //= 2

    if carry == 1:
        answer.append('1')
    answer.reverse()

    return ''.join(answer)
```
### Given read4 ii call multiple times
```python
class Solution(object):
    
    def __init__(self):
        self.temp_buf = [""] * 4
        self.offset = 0
        self.temp_available = 0
        
    def read(self, buf, n):
        total_read = 0
        eof = False
        
        while total_read < n and not eof:
           
            # keep reading
            if self.temp_available == 0:
                self.temp_available = read4(self.temp_buf)
            
                if self.temp_available < 4:
                    eof = True
            
            # lets update our temp_buf
            should_read = min(self.temp_available, n - total_read)
            
            for i in range(should_read):
                buf[total_read + i] = self.temp_buf[self.offset + i]
                
            
            total_read += should_read
            self.offset = (self.offset + should_read) % 4
            self.temp_available -= should_read
        
        return total_read
```
### Decode String 
```python
def decode_string(s) -> str:
    # create a stack
    stack = [["", "1"]]
    nums = ""

    for char in s:
        # [
        if char == "[":
            stack.append(["", int(nums)])
            nums = ""
        # ]
        elif char == "]":
            # process the stack
            top_string, top_k = stack.pop()
            stack[-1][0] += top_string * top_k

        # number
        elif char.isnumeric():
            nums += char
        # string
        else:
            # add to top of the stack
            stack[-1][0] += char

    return stack[0][0]
```
### Shortest Path in a Grid with Obstacles Elimination
```python
class Solution:
    def shortestPath(self, grid, k) -> int:
        rows = len(grid)
        cols = len(grid[0])
		# Directions we'll use to change our location (down, up, right, left).
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # We'll use a deque for our BFS traversal.
        q = collections.deque([])
		# Append our starting details to the q.
		# (row, col, steps, k)
        q.append((0, 0, 0, k))
		# Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
        seen = set()
        while q:
		    # Pop the next location from the q.
            r, c, steps, rk = q.popleft()
			# If we're at the finish location return the steps, given BFS this will be
			# guaranteed to be the first to hit this condition.
            if r == rows-1 and c == cols - 1:
                return steps
			# Otherwise we'll keep travelling throught the grid in our 4 directions.
            else:
                for y, x in directions:
                    nr = r + y
                    nc = c + x
					# If the new location is on the board and has not been visited.
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc, rk) not in seen:
					    # If it's a blocker but we still have k left, we'll go there and k -= 1.
                        if grid[nr][nc] == 1 and rk > 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk - 1))
						# Otherwise continue on  if it's a 0 - free location.
                        elif grid[nr][nc] == 0:
                            seen.add((nr, nc, rk))
                            q.append((nr, nc, steps + 1, rk))
		# If we don't hit the end in our traversal we know it's not possible.
        return -1
```
### K Closest Points to Origin    
```python
class Solution(object):
    def kClosest(self, points, K):
        # O(N log K)
        # O(K)
        solutions = []

        for point in points:
            current_distance = self.distance(point)

            if len(solutions) == K:

                heappush(solutions, (-current_distance, point))
                heappop(solutions)

            else:
                heappush(solutions, (-current_distance, point))

        return [heappop(solutions)[1] for _ in range(len(solutions))]

    def distance(self, point, origin=[0, 0]):

        p1, p2 = point
        q1, q2 = origin

        a = (q1 - p1) ** 2
        b = (q2 - p2) ** 2

        return math.sqrt(a + b)
```
### Dot Product of Two Sparse Vector 
```python
from collections import defaultdict

class SparseVector:
    def __init__(self, nums):

        self.compressed_vector = defaultdict(int)
        for i, element in enumerate(nums):
            if element:
                self.compressed_vector[i] = element

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        # a * b = A1B1 + A2B2
        solution = 0

        for column in vec.compressed_vector.keys():
            if column in self.compressed_vector:
                solution += self.compressed_vector[column] * vec.compressed_vector[column]

        return solution
```

### Sparse Matrix Multiplication  
```python
from typing import List

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        sparse_A = self.get_none_zero(A)
        sparse_B = self.get_none_zero(B)
        n, m, k = len(A), len(A[0]), len(B[0])
        C = [[0] * k for _ in range(n)]
        for i, j, val_A in sparse_A:
            for x, y, val_B in sparse_B:
                if j == x:
                    C[i][y] += val_A * val_B
        return C

    def get_none_zero(self, A):
        res = []
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    continue
                res.append((i, j, A[i][j]))
        return res
```
### Divide Two Integers
```python
def divide(dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    a, b = abs(dividend), abs(divisor)
    result = 0

    while a - b >= 0:
        x = 0
        while (a - (b <<  1 << x)) >= 0:
            x += 1
        result += 1 << x
        a -= b << x

    if not positive:
        result = -result
    return min(max(-2147483648, result), 2147483647)
```
### LRU Cache    
```python
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        # we can use orderedict to keep track of the recent get or put operation
        self.lru_dictionary = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # returns value from lru
        # updates location of lru
        if key not in self.lru_dictionary:
            return -1

        self.lru_dictionary.move_to_end(key)

        return self.lru_dictionary[key]

    def put(self, key: int, value: int) -> None:
        # if key already in lru then update location
        # if key not in lru then just add to the end
        # if by adding to lru we go over capacity then we can delete oldest

        if key in self.lru_dictionary:
            self.lru_dictionary.move_to_end(key)

        self.lru_dictionary[key] = value

        if len(self.lru_dictionary) > self.capacity:
            self.lru_dictionary.popitem(last=False)
```
### Monotonic Array   
```python
class Solution(object):
    def isMonotonic(self, A):
        increasing = True
        decreasing = True

        for i in range(1, len(A)):

            if A[i - 1] > A[i]:
                increasing = False

            if A[i - 1] < A[i]:
                decreasing = False

        return increasing or decreasing
```
### Candy Crush
```python
class Solution:
    def candyCrush(self, board):
        # start the while loop
        while True:
            # check for the candies to be crushed
            crush = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if j > 1 and board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}
                    if i > 1 and board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}

            # crush the candies.
            if not crush: break
            for i, j in crush:
                board[i][j] = 0

            # drop the candies
            for col in range(len(board[0])):
                idx = len(board) - 1
                for row in range(len(board) - 1, -1, -1):
                    if board[row][col] > 0:
                        board[idx][col] = board[row][col]
                        idx -= 1

                for row in range(idx + 1):
                    board[row][col] = 0

        return board
```
### Letter Combinations of a Phone Number  
```python
class Solution:
    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        output = []
        def recurse_back(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    recurse_back(combination + letter, next_digits[1:])

        
        if digits:
            recurse_back("", digits)
        return output
```
### asteroid-collision  
```python
def asteroid_collisions(asteroids):
    stack = []
    for a in asteroids:
        if a > 0:
            # append all positive numbers
            stack.append(a)
        else:

            # 1. if the top of the stack is going right and the current element is bigger
            while stack and stack[-1] > 0 and stack[-1] < abs(a):
                stack.pop()

            # stack is empty, previous is going same direction
            if not stack or stack[-1] + a < 0:
                stack.append(a)
            # if the current element is equal to the top the stack we explode both
            elif stack and stack[-1] + a == 0:
                stack.pop()

    return stack
```
### time-based-key-value-store
```python
from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        self.key_value_store = defaultdict(list) 

    def set(self, key, value, timestamp):
        self.key_value_store[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        # if no value? 
        if key in self.key_value_store:
            current_list = self.key_value_store[key]
            return self.find_closest_match(current_list, timestamp)
        else:
            return ""
        
    def find_closest_match(self, current_list, timestamp):
        # find value that has past_time <= timestamp
        # we can use binary search
        start = 0
        end = len(current_list) - 1
        
        while start < end:
            mid = (start + end + 1) / 2
    
            if current_list[mid][0] > timestamp:
                # prune right 
                end = mid - 1
            else:
                # prune left
                start = mid 
        
        if current_list[start][0] <= timestamp:
            return current_list[start][1]
        else:
            return ""
```
### friend-circles  
```python
class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        result = 0

        visited = set()
        for i in range(n):
            if i in visited:
                continue
            self.dfs(isConnected, i, visited)
            result += 1

        return result

    def dfs(self, isConnected, k, visited):
        visited.add(k)

        for i in range(len(isConnected[k])):
            if i in visited or isConnected[k][i] != 1:
                continue
            self.dfs(isConnected, i, visited)


print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))~~~~
```
### valid-parentheses 
```python
class Solution(object):
    def isValid(self, s):
        stack, match = [], {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in match:
                # stack should have closing bracket on top

                if stack and stack[-1] == match[char]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(char)

        return not stack
```
### product-of-array-except-self
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build left to right product
        # [1, 1, 2, 6]

        left = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]

        right = 1
        for j in reversed(range(len(nums))):
            left[j] = right * left[j]
            right *= nums[j]

        return left
```
### string-compression
```python
class Solution:
    def compress(self, chars) -> int:
        length = 0
        count = 1
        chars.append("\n")  # For last char

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
                continue

            # Write char
            chars[length] = chars[i - 1]
            length += 1

            if count == 1: continue
            # Write digis
            for n in str(count):
                chars[length] = n
                length += 1

            # Reset counter
            count = 1

        return length
``` 
### design-hit-counter
```python
class HitCounter(object):

    def __init__(self):
        self.myhits = [(0, 0)] * 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        # time difference
        location_hit = timestamp % 300

        current_time, current_count = self.myhits[location_hit]

        if timestamp - current_time < 300:
            self.myhits[location_hit] = (timestamp, current_count + 1)
        else:
            self.myhits[location_hit] = (timestamp, 1)

    def getHits(self, timestamp):
        count = 0

        for current_time, current_count in self.myhits:
            if timestamp - current_time < 300:
                count += current_count

        return count
```
### logger-rate-limiter
```python
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        if message not in self._msg_dict:
            # case 1). add the message to print
            self._msg_dict[message] = timestamp
            return True

        if timestamp - self._msg_dict[message] >= 10:
            # case 2). update the timestamp of the message
            self._msg_dict[message] = timestamp
            return True
        else:
            return False
```
### number-of-distinct-islands
```python
class Solution(object):
    def numDistinctIslands(self, grid):
        seen = set()
        def explore(r, c, r0, c0):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add((r - r0, c - c0))
                explore(r+1, c, r0, c0)
                explore(r-1, c, r0, c0)
                explore(r, c+1, r0, c0)
                explore(r, c-1, r0, c0)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c, r, c)
                if shape:
                    shapes.add(frozenset(shape))
        return len(shapes)
```
### design-hashmap
```python
class MyHashMap(object):

    def __init__(self):
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]


    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)


    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)


    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)
```

# Time based key value store

```python
from collections import defaultdict
class TimeMap(object):
    
    # We can use a hashmap that maps to an array
    
    # for get operations we can use binary search to find the desired timestamp 
    # we don't know what timestamp get is going to use
    

    def __init__(self):
        self.key_value_store = defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.key_value_store[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        # if no value? 
        if key in self.key_value_store:
            current_list = self.key_value_store[key]
            
            return self.find_closest_match(current_list, timestamp)
        else:
            return ""
        
    
    def find_closest_match(self, current_list, timestamp):
        # find value that has past_time <= timestamp
        # we can use binary search
        # todo: edgecase: if no valid values return ""
        start = 0
        end = len(current_list) - 1
        
        while start < end:
            mid = (start + end + 1) / 2
            
            
            if current_list[mid][0] > timestamp:
                # prune right 
                end = mid - 1
            else:
                # prune left
                start = mid 

        
        if current_list[start][0] <= timestamp:
            return current_list[start][1]
        else:
            return ""
```
