import heapq
def meetingRoomsII(intervals:list):

    intervals.sort(key= lambda x : x[0])

    ends = []
    rooms = 0

    for start,end in intervals:

        while ends and ends[0] <= start:
            heapq.heappop(ends)

        heapq.heappush(ends,end)

        rooms = max(rooms,len(ends))

    return rooms

intervals = [[0,30],[2,5],[4,6],[7,11]]

print(meetingRoomsII(intervals))