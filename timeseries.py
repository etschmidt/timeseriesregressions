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
'''
#inital plot
df.plot(figsize=(20,10), linewidth=5, fontsize=20)

plt.xlabel('Year', fontsize=20)
'''
diet = df[['diet']]
gym = df[['gym']]
#diet.rolling(12).mean().plot(figsize=(10,5), linewidth=5, fontsize=10)

#combines two series on same plot
df_rm = pd.concat([diet.rolling(12).mean(), gym.rolling(12).mean()], axis=1)

# .diff() only looks at the difference bewteen each data point an the point before it
# df.plot(figsize=(10,5), fontsize=10)


# print(df.corr())

# #something about crrelation
# from sklearn import datasets
# iris = datasets.load_iris()
# df_iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
#                      columns= iris['feature_names'] + ['target'])
# sns.lmplot(x='sepal length (cm)', y='sepal width (cm)', fit_reg=False, data=df_iris, hue='target')

# print(df_iris.groupby(['target']).corr())


# although the initial plot had negative correlation
# the differences were positivie because this removes
# the trend of seasonality
# df.diff().plot()

# plt.xlabel('Year', fontsize=10)
# plt.show()
# print(df.diff().corr())

pd.plotting.autocorrelation_plot(diet)
plt.show()

# The dotted lines in the above plot actually tell you about the statistical 
# significance of the correlation. In this case, you can 
# say that the 'diet' series is genuinely autocorrelated with 
# a lag of twelve months.