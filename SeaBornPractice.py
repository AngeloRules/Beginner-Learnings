import seaborn as sns
## Seaborn allows us to make visually stunning statistical plots
#import matplotlib.pyplot as plt
#tips = sns.load_dataset('tips')
#flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')

# nc = flights.pivot_table(index='month',columns='year',values='passengers')
# print(nc)
#dc = tips.corr()

## DISTRIBUTION PLOTS
#son = tips.head()
#sns.distplot(tips['total_bill'],kde=False,bins=30) #creates a univarient distribution plot, with a kde
#sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde') #plots two specified variables on a scatter plot
#sns.pairplot(tips,hue='smoker',kind='hex') # allows us to see scatter plots of all the pairs of columns in the dataset
#sns.rugplot(tips['total_bill'])# creates a sort of tally of the frequency of the variable

## CATEGORICAL PLOTS
#sns.barplot(x='sex',y='tip',data=tips)# shows the average of a selected number of
#sns.countplot(x='smoker',data=tips)#counts the frequency of each item and displays it on a barchart
#sns.boxplot(x='day',y='total_bill',data=tips, hue='smoker')# in a box plot the dots are outliers, the top and bottom whiskers stand for the upper and lower quartiles
#sns.violinplot(x='day',y='total_bill',data=tips, hue='sex',split=True)# violinplots show the kde of the underlying distribution
#sns.stripplot(x='sex',y='tip',data=tips) # shows a scatter plot of the data points
#sns.factorplot(x='day',y='total_bill',data=tips, kind='bar') # a more generalized form of the above plots

## MATRIX PLOTS

# matrix plots are only useful when when the data to be represented has some sort of matrix format

## heatmaps(cluster matrix)
#sns.heatmap(nc,annot=True,cmap='coolwarm',linecolor=,linewidths=)
#sns.clustermap(nc, cmap='coolwarm',standard_scale=1) # tries to cluster similar data points together

## GRIDS
tr = iris.head()
print(tr)

#plt.show()
