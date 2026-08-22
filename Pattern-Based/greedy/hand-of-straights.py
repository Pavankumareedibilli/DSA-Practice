from collections import Counter
def handOfStraights(hand:list,groupSize)->bool:

    if len(hand)%groupSize != 0:
        return False
    
    count = Counter(hand)

    for card in sorted(count):
        if count[card] == 0:
            continue

        groups = count[card]
        
        for x in range(card,card+groupSize):
            if count[x] < groups:
                return False

            count[x] = count[x] - groups

    return True
            

hand = [1,2,3,6,2,10,4,7,8]
groupSize = 3

print(handOfStraights(hand,groupSize))