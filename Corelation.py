import pandas as pd

data=[[17,150],
      [15,154],
      [19,169],
      [17,172],
      [21,175]]

df = pd.DataFrame(data, columns=["Hand","Height"])

print(df.corr())
