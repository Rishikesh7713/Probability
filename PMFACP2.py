import scipy.stats as stats

prob=1-stats.binom.cdf(12, 30, 0.5)

print("The probability of getting more than 12 rainy days in 30 days : ", prob)

prob1=stats.poisson.pmf(12, 30)
print("Probability of raining for exactly 12 days : ", prob1)

prob2=stats.poisson.pmf(18, 30)
print("Probability of raining for exactly 18 days : ", prob2)