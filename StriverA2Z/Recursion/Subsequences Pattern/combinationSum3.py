def combinationSum3(k:int,n:int):
    result = []

    def backtrack(start,path,curr_sum):
        if len(path) == k:
            if curr_sum == n:
                result.append(path[:])
                return
        
        if curr_sum>n:
            return
        
        for i in range(start,10):
            if curr_sum + i>n:
                break
            
            path.append(i)
            backtrack(i+1,path,curr_sum+i)
            path.pop()
        
    backtrack(1,[],0)
    return result


print(combinationSum3(3,7))