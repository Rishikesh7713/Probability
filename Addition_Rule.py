def prob_a_or_b(a, b, all_possibble_outcome):
    prob_a=len(a)/len(all_possibble_outcome)

    prob_b=len(b)/len(all_possibble_outcome)

    inter=a.intersection(b)

    prob_inter=len(inter)/len(all_possibble_outcome)

    return (prob_a + prob_b - prob_inter)
            
evens={2, 4, 6}
greterthan2={3, 4, 5, 6}
allpossiblerolls={1, 2, 3, 4, 5, 6}

print("Probability of Getting an Even no or a no greater than 2")
print(prob_a_or_b(evens, greterthan2, allpossiblerolls))