
from scipy.stats import chi2_contingency

data = {
  "Ed Level": ["High School", "Bachelors", "Masters", "Ph.D."],
  "Female": [60, 54, 46, 41],
  "Male": [40, 44, 53, 57]
}

ct = [data["Female"], data["Male"]]

chi2, pval, degrees_of_freedom, expected_frequency = chi2_contingency(ct)

print("Chi-Square Statistic:", chi2)
print("p-value:", pval)
print("Degrees of Freedom:", degrees_of_freedom)

# Hypothesis Testing at 5% significance level (alpha = 0.05)
if pval < 0.05:
    print("Reject Null Hypothesis - Gender and Education Level are dependent.")
else:
    print("Fail to Reject Null Hypothesis - Not enough evidence for dependence.")
