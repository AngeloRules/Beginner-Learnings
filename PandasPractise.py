import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)

# # series
# # series in pandas are built on a numpy object
# # the can however be labelled and accessed by that label
# # the pandas.Series() method automatically transforms dictionary key-value pairs into a series
# # indexing in panda series works like a dictionary or hash table thus making look ups very fast
# # data = [10, 20, 30]
# # labels = ['a','b','c']
# #noob = pd.Series(data=data,index=labels)

# #data frames

# # the index is similar to the rows
# #
# df = pd.DataFrame(data=randn(5,4),index=['A','B','C','D','E'],columns=['W','X','Y','Z'])
# # the columns form pandas series
# # pandas frames are series that share a common index
# print(df['W']['A'])
#
# # to remove columns we use the df.drop() method
# print(df[['X','Y']])# to select multiple columns from a data frame we pass a list of lists
# df['new'] = df['X'] + df['X']
# print(df.drop('new',axis=1,inplace=True))# this method doesnt create a new object
# # to make the deletion permanent we have to specify a value of the argument "inplace"
# # when we apply the .drop method we need to specify the value of the axis
# # rows take the 0 axis
# # columns take the 1 axis
# # to index rows we can use the .loc[] method
# print(df.loc['E']) # indexing using the loc[] method
# print(df.iloc[4]) # we can use the index itself
# print(df.loc[['A','B'],['X','Y']])# to grab a subset of the dataframe
#
# # like numpy arays pandas data frames support conditional selection
# print(df[(df['W'] > 0) | (df['Y'] < 1)]) # 'and' in the pandas library is '&'
# # 'or' in the pandas library is '|'
# # in order to reset the indicies of a data frame we use the .reset_index() method
# print(df[df['W']>0][['Y','X']])
# sttes = "ABJ KWA LGA OYO OND"
# states = sttes.split()
# df['States'] = states
# print(df)
# # to make a particular row the new index we can use the .set_index() method
# dg = df.set_index('States',inplace=True)
## MultiLevel Indexing (Index Hiearchy)
# outside = ['G1','G1','G1','G2','G2','G2']
# inside = [1,2,3,1,2,3]
# hier_index = list(zip(outside,inside)) # the zip function takes two arguments and makes tuples
# hier_index = pd.MultiIndex.from_tuples(hier_index)
# df = pd.DataFrame(data=randn(6,2),index=hier_index,columns=['A','B'])
#
# print(df.loc['G1'].iloc[0]) # when indexing a multilevel dataframe, we first grab the first column then work our way inwards
# df.index.names = ['Groups','Numbers'] #assigning index names to the levels of indicies
# #df.index.names =
# # to get a cross section of a data frame we can use the .xs() method
# # it is useful most especially for multilevel indicies
# print(df)
# print(df.xs())
# print(df.loc['G2'].iloc[1]['B'])
# print(df.xs(1,'Numbers'))

## Missing Data
# d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
# df = pd.DataFrame(data=d)
# df['Names'] = 'N1','N2','N3'
# df.set_index('Names',inplace=True)
# ## to drop rows or columns containing missing values we use the .dropna() methods
# ## to drop rows we use 'axis = 0' argument , and to drop columns we use 'axis = 1'
# ## the 'thresh'argument sets the minimum number of NaNs necessary to avoid removal
# df.dropna(axis=0,thresh=1,inplace=False)
# ## to fill in missing values we can use the .fillna() method
# df.fillna(value=df.mean(),inplace=True)
# print(df)

## Creating Groups
## to create groups we use the method .groupby()

# data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
#         'Person':['Sam','Charlie','Amy','Vanessa','Carl','Smith'] ,
#         'Sales':[200,250,400,560,300,123] }
# names = 'N1 N2 N3 N4 N5 N6'
# df = pd.DataFrame(data=data,index=names.split())
# df.index.names = ["Names"]
# byCompany = df.groupby("Company")
# print(byCompany.count())
# .max(),.min(),.describe(),.sum(),.transpose()
## the .describe() method is used to give a summary of data in the cell
## after assigning a variable name we can apply different methods

## Merging, Joining and Concatenating Dataframes
## concatenation stitches two data frames toghther
## we use pd.concat([df1,df2,df3])
## while concatenating, the data frames in question must be of the same size
## pd.concat() takes the argument 'axis' to specify where the joining is taking place

## merging combines two data frames togehter however it takes the arguments ,'how' and 'on'
## 'key' tells us where the merge takes place
##pd.merge(value=,key=,how=,on=[])

## joining
## this helps us to combine two  differently indexed data frames together
## df1.join(df2)

## operations
## below are some useful operations that can be carried on pandas data frames
## .unique() - a method used to find unique elements in a pandas data frame
## .nunique() - a method used to find number of unique elements in a pandas data frame
## .value_counts() - a method to find the number of occurences of an item in a data frame
## .apply() - allows us to apply our custom made functions to pandas data frames, it
## also lets us apply built in functions

## .columns - returns a list of columns in a pandas data frame
## .index - returns a list of indicies in a data frame
## .sort() - allows us to sort a data frame by whatever parameter is in the argument
## .isnull() - returns the null values in a pandas dataframe

## .pivot_table() - allows us to create pivot tables from our data, it takes three main arguments
## they are 'value','index','columns'

## Data Input and Output
