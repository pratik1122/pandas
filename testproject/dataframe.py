import pandas as pd


p1 = pd.read_csv('exams.csv',index_col= 'gender')

print(p1.head(1))
print(p1.tail(1))
print(p1.index)
print(p1.shape) #   number od rows and columns

print(p1.dtypes) # datatype of  all column

print(p1.columns)  # returns all the columns

print(p1.info())   # returns columns with number of not null values

print(p1.get_dtype_counts()) # retruns datypes and number of columns with that datatype

# sum pf numbers horizontally

                                                                       #####     SUM

print(p1.sum(axis = 1).head(20))

print(p1.sum(axis='columns').head(7))

print(p1.sum(axis ='columns').tail(5))

                                                                     ###  SELECT COLUMN
#SELECT ONE COLUMN FROM DATAFRAME

print(p1['math score'].head(7))

#SELECT two or more column from a dataframe

print(p1[ ['math score','reading score'] ])

# sor values on selected  columns

print(p1[ ['math score','reading score'] ].sort_values(by =['math score'],ascending= True).head(7))


# ADD NEW COLUMN

p1['sports'] = 'cricket'


#ADD NEW COLUMN IN PURTICULAR POSITION

p1.insert(3,column = 'height', value = 'good')

print(p1.head(2))

#BROADCATING OPERATIONS


# ADD MUL DIVIDE  MARKS TO EVERY ROW IN MATH SCORE

print(p1['math score'].head(7))
#p1[' math score'] += 7
p1.insert(2,column='physics score',value =p1['math score'] /2)
print(p1.head(7))



#   .value_counts() method

print(p1['lunch'].value_counts().head(1))  # means number of repetitions


print(p1.tail())


#  DELETE ROW WITH NULL VALUES
#mana
# p1.dropna() # deletes rows any single null values
#
# p1.dropna(how = all) # deletes only rows with all null values)
#
# p1.dropna(subset =['math score','physics score'])


# fillna method

p1['math score'].fillna(23,inplace =True)  # insert value to null values in that purticular column
print(p1.head(3))

#  ASTYPE METHOD ( TO CONVERT DATATYPE OD A COLUMN)

print(p1.dtypes)
print(p1.info())


p1['math score']= p1['math score'].astype('float')
print(p1.info())


print(p1['lunch'].nunique())


#  sort method in dataframe


print(p1.sort_values(by=['math score'],ascending = False).head(7))


# sort mutiple columns

print(p1.sort_values(['math score','physics score'],ascending= [True,False],inplace = True))



#sort_index() method

print(p1.sort_index(ascending = True).head())


# Rank Method

print(p1['math score'].rank(ascending = False).astype('int').head())




 ########################################### DATAFRAME 2 #############################################
#
#
# p1['start date'] = 1/1/2011
# p1['start date'] = pd.to_datetime(p1['start date'])
#
#
# print(p1.head())


                                                                                #  date time object

print(p1.head(20))


# APPLYING FILTER ON DATAFRAMES


mask1 = p1['math score'] > 70
mask2 = p1['lunch'] == 'standard'
mask3 = p1['reading score'] >50

print(p1[(mask1 & mask3)| mask2 ].tail(20))


# isin method
mask7 = p1['math score'].isin([81.0,82,83,84])
print(p1[mask7])


#isnull and not null method

maskn = p1['lunch'].isnull()
print(p1[maskn])


masknn = p1['lunch'].notnull()
print(p1[masknn].head())


# between method

tomb = p1['math score'].between(40,70)
print(p1[tomb])

# duplicate method

tomb1 = p1['math score'].duplicated(keep = 'last')
print(p1[tomb1])

#               drop duplicate Method
#
# tomb1 = p1['math score'].drop_duplicates() # deletes if all  column values match thus no
#
# print(p1.drop_duplicates(subset=['math score'],keep='first'))

# unique and nunique methods
print(p1['math score'].unique())
print(p1['math score'].nunique(dropna=False))
print(p1['physics score'].unique())

########################################     DATAFRAME3  ##########################################333

# .set_index and reset_index methods
p1.reset_index(inplace = True)
print(p1)

### first reset index  to numbers abd the assign any colun to index



print(p1.head())
p1.set_index('lunch',inplace= True)
print(p1.head())

print(p1.reset_index(inplace = True))
print(p1)


p1.set_index('gender',inplace = True)
print(p1)


# loc method   for locating object but it should be an index object


p1.reset_index(inplace = True)
print(p1)

print(p1.iloc[ [10,20]]) # locates multiple object
print(p1.loc[ [22,33,44] ])


# catch all method
#.ix Method to find the location


print(p1.ix[[22,33,11]])
print(p1.ix[[10,21,25],['math score','physics score']])


# set new value for specific row or column
p1.ix[ 10,['math score','physics score']]=[88,89]
print(p1.ix[10])


# rename and rename index columns

p1.rename(columns = {'math score':'maths score'},inplace= True)
print(p1.head())



# drop column or rows in dataframe

del p1['height']

print(p1.head())



# SAMPLE Parameter


p1.sample(n=4)

print(p1.head())


p1.sample(frac= .20)

print(p1.head())

          #  Copy method


# study query
p2 = p1['maths score'].copy()
print(p2.head(3))



                ###############  WORKING WITH TEXT DATA  ############




print(p1['sports'].str.upper())

print(p1['sports'].str.title())

print(p1['sports'].str.len())

print(p1['sports'].str.replace('e','k'))

print(p1['sports'].str.contains('cri'))


print(p1['sports'].str.startswith('cri'))


print(p1['sports'].str.endswith('cri'))

print(p1['sports'].str.strip())


print(p1['sports'].str.lstrip())


print(p1['sports'].str.rstrip())
p1['sports'] = p1['sports'].str.upper()



##########  string methods on index and columns  ##########3

p1.columns = p1.columns.str.upper()
print(p1.head())

p1.columns = p1.columns.str.lower()
print(p1.head())

p1['sports1'] = p1['sports'].str.split(',')

#multiindex  module

