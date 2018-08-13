import numpy as np
import pandas as pd

'''
data = np.array([['', 'Col1', 'Col2'], 
				['Row1', 1, 2],
				['Row2', 3, 4]])
print(pd.DataFrame(data=data[1:,1:],
				   index=data[1:,0],
				   columns=data[0,1:]))
'''
'''
# 2d-array
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))

# dictionary
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}

# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(pd.DataFrame(my_df))

# Take a Series as input to your DataFrame
my_series = pd.Series({"Belgium":"Brussels", "India":"New Delhi", 
	"United Kingdom":"London", "United States":"Washington"})
print(pd.DataFrame(my_series))
'''

# df= pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index=[0, 1, 2], columns=['A', 'B', 'C'])

# print(df)
# shape is rows by columns
#print(df.shape)

# len() gives numbers of rows in index
#print(len(df.index))
'''

.loc references the name
.iloc references the position

print(df.iloc[0][0])

print(df.loc[0]['A'])

print(df.at[0, 'A'])

print(df.iat[0, 0])

print(df.iloc[0])
print(df.loc[:,'A'])


df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index= [2, 'A', 4], columns=[48, 49, 50])

df.iloc[2] = [60, 50, 40]
df.loc[2] = [11, 12, 13]
print(df)

'''
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])

df["D"] = df.index

print(df)