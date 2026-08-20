def lemonade_change(bills:list)->bool:
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives = fives +1

        elif bill == 10:
            if fives> 0:
                fives = fives - 1
                tens = tens + 1
            else:
                return False

        else:
            if fives > 0 and tens > 0:
                fives = fives - 1 
                tens = tens -1
            elif fives > 3:
                fives = fives - 3
            else:
                return False
    return True

bills = [5,5,10,5,10,20]
print(lemonade_change(bills))