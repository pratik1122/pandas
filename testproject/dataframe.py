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
#
# p1.dropna() # deletes rows any single null values
#
# p1.dropna(how = all) # deletes only rows with all null values)
#
# p1.dropna(subset =['math score','physics score'])


