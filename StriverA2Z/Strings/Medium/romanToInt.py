def romanToInt(s:str)->int:

    values ={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }

    Ans = 0
    prev_value = 0

    for ch in reversed(s):
        curr_value = values[ch]

        if curr_value < prev_value:
            Ans -= curr_value
        else:
            Ans = Ans + curr_value

        prev_value = curr_value

    return Ans


s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"

print(romanToInt(s1))
print(romanToInt(s2))
print(romanToInt(s3))




