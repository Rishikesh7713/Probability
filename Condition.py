def a_and_b(a, b):
    if a ==1:
        prob_student=0.3
        if b==1:
            prob_dining=0.75
        else:
            prob_dining=0.25
        print("Proability of given b : ", prob_dining)

    if a ==2:
        prob_student=0.7
        if b==1:
            prob_dining=0.6
        else:
            prob_dining=0.4
        print("Probability of given b : ", prob_dining)

    prob_a_and_b=prob_student*prob_dining
    return round(prob_a_and_b, 3)

print("Check the Probabilty of any event occuring. First enter your choices")

print("Is the student Freshman? \n1. Yes\n2. No")
a=int(input("Enter your Choice (1/2) : "))

print("Is the student eating in dining hall?\n1. Yes\n2. No")
b=int(input("ZEnter your Choice (1/2)"))

print("Here is the probability of both events occuring : ", a_and_b(a, b))