import pandas as pd
#bab = pd.read_csv('/Users/user/Desktop/Progress/1/Udemy - Python for Data Science and Machine Learning/6. Python for Data Analysis - Pandas/03-Python-for-Data-Analysis-Pandas/example')
#dab = pd.read_excel('/Users/user/Desktop/Progress/1/Udemy - Python for Data Science and Machine Learning/6. Python for Data Analysis - Pandas/03-Python-for-Data-Analysis-Pandas/Excel_Sample.xlsx', sheet_name='Sheet1')
## the read command allows us to read from a variety of file formats
## .to_ allows us to write to a variety of formats
# df = pd.DataFrame(data=dab)
# df.to_excel('/Users/user/Desktop/SAMMY.xlsx',sheet_name='SAM',index=False)
datas = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
df = pd.DataFrame(data=datas[0])
print(df.groupby('Name'))

