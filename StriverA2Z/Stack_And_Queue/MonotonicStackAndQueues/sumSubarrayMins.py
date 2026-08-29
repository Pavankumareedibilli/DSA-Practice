def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        stack = []
        ans = 0

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        
        stack.clear()

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller[i] - i
            ans =(ans + left*right*arr[i]) % MOD
        
        return ans 