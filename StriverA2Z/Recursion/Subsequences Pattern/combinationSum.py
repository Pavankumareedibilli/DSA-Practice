def combinationSum(candidates,target):
    result = []
    def dfs(start,target,path):
        if target == 0:
            result.append(path[:])
            return

        for i in range(start,len(candidates)):
            if candidates[i]>target:
                continue

            path.append(candidates[i])

            dfs(i,target-candidates[i],path)

            path.pop()
    dfs(0,target,[])

    return result

candidates = [2, 3, 6, 7]
target = 7

print(combinationSum(candidates, target))
