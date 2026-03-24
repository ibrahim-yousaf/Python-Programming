#Create Dataframe
import pandas as pd
import numpy as nd
my_file = pd.DataFrame([[10,20,30],[100,200,300],[100,200,300]])
print(my_file)
#Create DataFrame with rows and column
my_file = pd.DataFrame([[10,20,30],[100,200,300],[100,200,300]],['Row1','Row2','Row3'],['Col1','Col2','Col3'] )
print(my_file)
#Create DataFrame with Dictionary
d = {
    "person1" :
{"name" : "Qadir",
 "Salary" : 12000,
 "Profile" : "SD1"},
    "person2" :
{"name" : "Mahmood",
 "Salary" : 11000,
 "Profile" : "SD2"},
    "person3" :
{"name" : "Fazil",
 "Salary" : 14000,
 "Profile" : "SD3"}
}
d_file = pd.DataFrame(d)
print(d_file)
#Create DataFrame using Numpy
dnum = pd.DataFrame(nd.arange(1,51).reshape(10,5),
['Row1','Row2','Row3','Row4','Row5','Row6','Row7','Row8','Row9','Row10'],
['Col1','Col2','Col3','Col4','Col5'])
print(dnum)
#Type
print(type(dnum))
#Info
print(dnum.info())
#Top and Bottom Data
print(dnum.head())
print(dnum.tail())
#Describe
print(dnum.describe())
#Column
print(dnum['Col1'])
#Multiple Columns
print(dnum[['Col1','Col3']])
#Row
print(dnum.loc['Row1'])
#Multiple Rows
print(dnum.loc[['Row1','Row2']])
#save dataset as csv file
dnum.to_csv('test.csv')
print(dnum)
#Pandas Read CSS
df = pd.read_csv('test.csv')
print(df)
print(df.describe())
