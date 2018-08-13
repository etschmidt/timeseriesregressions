import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
#only for jupyter notebooks
#%matplotlib inline
sns.set()

#import and skip the top rows
df = pd.read_csv('data/multiTimeline.csv', skiprows=1)

# assign column headings
df.columns = ['month', 'diet', 'gym', 'finance']

#turn month column into datetime format
df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)

df.plot(figsize=(20,10), linewidth=5, fontsize=20)

plt.xlabel('Year', fontsize=20)

plt.show()