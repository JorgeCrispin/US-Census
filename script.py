import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob
import re

files = glob.glob("states*.csv")
 
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
us_census = pd.concat(df_list)  

print(us_census.columns)
print(us_census.dtypes)
print(us_census.head())
no_dollar_sign = []
for value in us_census.Income:
  no_dollar_sign.append(value.replace('$', ''))
Income_working_numbers=[]
for string_ in no_dollar_sign:
  Income_working_numbers.append(float(string_))  
us_census['Income'] = Income_working_numbers


male_female_split = []
for item in us_census.GenderPop:
  male_female_split.append(item.split('_'))
Male_pop = []
Female_pop = []
count = 0
for i in range(len(male_female_split)):
  Female_pop.append(male_female_split[i][1])
  Male_pop.append(male_female_split[i][0])
us_census['Male'] = Male_pop
us_census['Female'] = Female_pop

male_pop = []
for item in us_census.Male:
   item.replace('M','')
female = []
male = []
for item in us_census.Female:
  female.append(item.replace('F',''))
for item in us_census.Male:
  male.append(item.replace('M', ''))    
#print(female)
#print(male)
us_census['Male'] = male
us_census['Female'] = female
floating_male = []
floating_female = []
for item in us_census.Male:
  item = float(item)
  floating_male.append(item)
#for item in us_census.Female:
  if item == '':
    continue
  else:
    item = float(item)
    floating_female.append(item)

us_census['Male'] = floating_male
#us_census['Female'] = floating_female
us_census['Female'] = pd.to_numeric(us_census['Female'])
print(us_census.dtypes)
print(us_census.head())
plt.scatter(us_census['Female'], us_census['Income'])
plt.show()
us_census['Women'] = us_census['Female'].fillna(us_census['TotalPop']-us_census['Male'])
us_census.drop(columns = 'Female', inplace=True)
print(us_census.duplicated())
print(us_census.head())
plt.scatter(us_census['Women'], us_census['Income'])
plt.show()

hispanic = []
white = []
black = []
native = []
asian = []
pacific = []

for item in us_census.Hispanic:
  hispanic.append(item.replace('%',''))
for item in us_census.White:
  white.append(item.replace('%', ''))
for item in us_census.Black:
  black.append(item.replace('%',''))
for item in us_census.Native:
  native.append(item.replace('%', ''))     
for item in us_census.Asian:
  asian.append(item.replace('%',''))
for item in us_census.Pacific:
  if type(item) == float:
    #item = str(item)
    #print(item)
    pacific.append(item)
  else:
    pacific.append(item.replace('%',''))

us_census['Hispanic'] = hispanic
us_census['White'] = white
us_census['Black'] = black
us_census['Native'] = native
us_census['Asian'] = asian 
us_census['Pacific'] = pacific
us_census['Hispanic'] = pd.to_numeric(us_census['Hispanic'])
us_census['White'] = pd.to_numeric(us_census['White'])
us_census['Black'] = pd.to_numeric(us_census['Black'].fillna(0))
us_census['Native'] = pd.to_numeric(us_census['Native'].fillna(0))
us_census['Asian'] = pd.to_numeric(us_census['Asian'].fillna(0))
us_census['Pacific'] = pd.to_numeric(us_census['Pacific'].fillna(0.1))


print(us_census.head())
plt.hist(us_census.Pacific)
plt.hist(us_census.Hispanic)
plt.show()

plt.hist(us_census.Black)
plt.hist(us_census.White)
plt.show()
