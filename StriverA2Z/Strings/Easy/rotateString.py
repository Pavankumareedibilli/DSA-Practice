def rotateString(s:str,goal:str)->bool:
    doubled = s+s
    return goal in doubled

s = "pavan"
goal = "vanpa"

print(rotateString(s,goal))