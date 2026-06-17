def Reverse(text:str):
    reversed_str = ""
    for ch in text:
        reversed_str = ch + reversed_str
    return reversed_str

text = "Pavan"
print(Reverse(text))