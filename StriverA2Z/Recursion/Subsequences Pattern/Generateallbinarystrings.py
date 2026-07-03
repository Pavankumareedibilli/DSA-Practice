def generateBinaryStrings(n:int):
    ans = []
    def generate(curr):
        if len(curr) == n:
            ans.append(curr)
            return

        generate(curr+"0")

        if not curr or curr[-1] == "0":
            generate(curr + "1")

    generate("")
    return ans

n = 3
print(generateBinaryStrings(n))