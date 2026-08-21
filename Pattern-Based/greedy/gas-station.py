def canCircle(gas:list,price:list)->int:
    total_gas = 0
    current_gas = 0
    start = 0
    for i in range(len(gas)):
        difference = gas[i] - price[i]
        total_gas = total_gas + difference
        current_gas = current_gas + difference
        if current_gas < 0:
            start = i + 1
            current_gas = 0
    if total_gas < 0:
        return -1
    return start

gas = [1,2,3,4,5]
cost =[3,4,5,1,2]
print(canCircle(gas,cost))