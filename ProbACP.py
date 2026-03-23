import random

def dice_roll():
    nos=[1, 2, 3, 4, 5, 6]

    res=random.choice(nos)

    pro=nos.count(6)/len(nos)
    print("Probability of No 6 is : ", pro)

    if res==6:
        return "No 6 was Picked"
    else:
        return "Better Luck Next Time"
    
res=dice_roll()
print(res)