def minArrowsToBurstBalloons(balloons:list)->int:
    balloons.sort(key= lambda x : x[1])
    arrow = 0
    arrow_position = float("-inf")

    for start,end in balloons:
        if start > arrow_position:
            arrow = arrow +1
            arrow_position = end
    return arrow

balloons = [[10,16],[2,8],[1,6],[7,12]]
print(minArrowsToBurstBalloons(balloons))