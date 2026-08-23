def maxActivities(activities:list[list]) -> int:

    activities.sort(key= lambda x : x[1])

    count = 0
    last_finish = float("-inf")

    for start,finish in activities:
        if start>=last_finish:
            count = count + 1
            last_finish = finish
    return count

activities = [[1,2],[3,4],[0,6],[5,7],[8,9],[5,9]]
print(maxActivities(activities))