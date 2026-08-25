def maxArea(self, height: list[int]) -> int:
        left = 0 
        right = len(height)-1
        max_volume = float("-inf")
        while left<right:
            width = right - left
            length = min(height[left],height[right])
            max_volume = max(max_volume,width*length)
            
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right -1
        return max_volume