RS=int(input("Enter Number of Red shirts : "))
BS=int(input("Enter Number of Blue shirts : "))
WS=int(input("Enter Number of White shirts : "))

total=RS+BS+WS

prob_a=BS/total
prob_b=RS/total

prob_bga=prob_b
prob_a_and_b=prob_a*prob_b

print("Probability that the 2nd shirt is red given that the 1st shirt is blue : ")
print(round((prob_bga), 3))

print("Probability that the 2nd shirt is red and the 1st shirt is blue : ")
print(round((prob_a_and_b), 3))