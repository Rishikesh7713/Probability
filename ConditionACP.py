def prob_b_and_w(b, w, total):
    prob_b=black/total

    prob_wga=white/(total-1)

    prob_BandW=prob_b*prob_wga

    return round(prob_BandW, 3)

black=int(input("Enter Number of orange balls"))
white=int(input("Enter Number of Blue balls : "))
total=black+white

print("Probability of getting 1st White and 2nd White ball : ")
print(prob_b_and_w(black, white, total))