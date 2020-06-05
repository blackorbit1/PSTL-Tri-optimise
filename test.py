import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""
df = pd.DataFrame({'Property 1':['a']*100+['b']*100,
                   'Property 2': ['w', 'x', 'y', 'z']*50,
'Value': np.random.normal(size=200)})


ax = sns.boxplot(x='Property 2', hue='Property 1', y='Value', data=df)

X = np.repeat(np.atleast_2d(np.arange(4)),2, axis=0)+ np.array([[-.2],[.2]])

plt.show()

"""
nbrep = 2000
la = 0

for rep in range(nbrep):
    la = 0 if rep == 0 else (round((la + 0.0001), 4) if (rep % ((nbrep*3) / 1000)) == 0 else la)
    print(la, end="\t")

