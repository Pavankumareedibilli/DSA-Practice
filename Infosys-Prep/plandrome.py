def is_palindrome(text:str):
    left = 0
    right = len(text)-1

    while left<right:

        while left<right and not text[left].isalnum():
            left = left+1
        while left<right and not text[right].isalnum():
            right = right-1
        
        if text[left].lower() != text[right].lower():
            return False
        left = left +1
        right = right -1
    return True

text = "Ab1b1, B@a"

print(is_palindrome(text))
