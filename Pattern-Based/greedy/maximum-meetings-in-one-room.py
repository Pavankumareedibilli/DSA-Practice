def countMaximumMeetings(start:list[int],end:list[int])->int:
    meetings = [] #O(N)Space
    n = len(start)

    for i in range(n): #O(N)Time
        meetings.append([start[i],end[i]])

    meetings.sort(key= lambda x : x[1]) #O(NlogN)Time

    last_end = float("-inf")
    count = 0

    for start,end in meetings: #O(N)Time
        if start >= last_end:
            count = count + 1
            last_end = end
    return count

#Overall Time = O(N)+ O(NlogN)+ O(N) = O(NlogN)
#Overall Space = O(N)

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
print(countMaximumMeetings(start,end))