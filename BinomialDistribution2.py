import math
def binomial_probability(n,k,p):
            bin_coef=math.comb(n,k)
            prob=bin_coef*(p**k)*((1-p)**(n-k))
            return prob

n=6
k=4
p=0.25
prob_forsuc=binomial_probability(n,k,p)
print('probability of exactly 4 success',prob_forsuc)
prob_lsucc=1-binomial_probability(n,0,p)
print('probability of atleast 1 succes',prob_lsucc)
           
