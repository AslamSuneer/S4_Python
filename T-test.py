import numpy as np
from scipy.stats import t
sammean,sd,n,popmean,p=22,3,16,20,0.05
t_ob=(sammean-popmean)/(sd/np.sqrt(n))
df=n-1
crit_t=t.ppf(1-p,df)

print("Observed Value: ",t_ob)

print("Table Value: ",crit_t)

if np.abs(t_ob)>crit_t:
	print("Reject NULL Hypothesis.")
else:
	print("Failed to Reject NULL Hypothesis.")

