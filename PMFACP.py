import scipy.stats as stats

prob_1=stats.binom.pmf(2, 10, 0.5)
print("Probability of getting 2 heads : ")
print(prob_1)

prob2=stats.binom.pmf(4, 10, 0.5)
print("Probability of getting 4 heads")
print(prob2)