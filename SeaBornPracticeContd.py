## GRID PLOTS
## unlike pair plots which plots all the pairwise relationships in a dataset
## pairgrids give us the option to control what kind  of plot we haveon the grid
import seaborn as sns
import matplotlib.pyplot as plt
#iris = sns.load_dataset('iris')

tips = sns.load_dataset('tips')
## PAIRGRID
# ar = sns.PairGrid(iris)
# ar.map(plt.scatter)
# ar.map_diag()
# ar.map_upper()
# ar.map_lower()
## FACETGRID
# ar = sns.FacetGrid(data=tips,col='time',row='smoker') # creates a grid with time as the column and smoker as the row
# ar.map(sns.distplot,'total_bill')#creates a distribution plot of the total bill on the grid

## REGRESSION PLOT
#sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
## COLOR AND STYLE
sns.set_style('whitegrid') #takes arguments 'ticks', 'darkgrid', 'lightgrid'
sns.countplot(x='sex',data=tips)
sns.despine(top=True,right=True) ## used to remove the boarders from a figure
plt.figure(figsize=(12,2)) 
## to change figure size and aspect ratio we can use either plt.figure(figsize=())
## or we can use matplotlibs inbuilt
plt.show()
