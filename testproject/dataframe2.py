import pandas as pd

p1 = pd.read_csv('studetails.csv',parse_dates= ['DOB'],index_col =['Gender','DOB'])
print(p1.head(33))
p1.sort_index(ascending=True)
#
# del p1['TotalWorkingYears']
#
# del p1['TrainingTimesLastYear']
# del p1['WorkLifeBalance']
# del p1['YearsInCurrentRole']
# del p1['RelationshipSatisfaction']
# del p1['StockOptionLevel']
# del p1['YearsSinceLastPromotion']
# del p1['YearsWithCurrManager']
# del p1['DistanceFromHome']
#
# print(p1.head())
# print(p1.dtypes)
# p1.set_index('DOB',inplace=True)
# print(p1.head())
# p1.reset_index(inplace= True)
# print(p1.head())
#
#
# #########   CREATING MULTI INDEX COLUMN
#
# p1.reset_index(inplace= True)
# p1.set_index(keys=['Gender','DOB'],inplace= True)
# print(p1.head())
# print(p1.index[0])
#
#
# ## .get_level_values()
#
# p1.sort_index(ascending=True)
#
# print(p1.head())



#   get_level_values method
print(p1.index.get_level_values(1))



# set_names method
print(p1.index.set_names(['Race','DOB'], inplace = True))
print(p1.head())


# sort_index method

p1.sort_index(ascending=[False,True],inplace= True,)
print(p1.head())

# extract rows from mutiindex dataframe

print(p1.ix[('M','1988-05-04'),'Biology']) # use ix method  toset the tuple to extract data from multiindex values

# .transpose method
K1=p1.transpose() # change vertial axis horizontal to vertical and vice versa
print(K1.ix['Physics',('M','1987-04-05')])



## THE SWAPLEVEL METHOD

l1 = p1.swaplevel()
print(l1.head())           #   swaps the index

# stack method

print(p1.stack())          #swaps the columns


print(p1.unstack().unstack()) #  stack =  values to rows
                              # unstack = values to columns


ss1 = p1.stack()
print(ss1.head())

print(ss1.unstack(-1))
print(ss1.unstack('DOB'))
print(ss1.unstack(0))


#  unstack two columns

print(ss1.unstack(level= [1,0]))

# pivot method

print(p1.head())
#
# pp1 =p1.pivot(columns='DOB')
# print(pp1.head())


o1= pd.read_csv('studetails.csv')


print(o1.head())
#print(o1.pivot(index = 'Gender',columns=))

print(o1.pivot_table(index='DOB',columns= 'Maths',values='Physics',aggfunc = 'mean'))  # frameing table

                                                         # Melt Method  Nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn


#####3   GROUPBBY OBJECT ##


df  = pd.read_csv('exams.csv')

print(df.head())
print(df.shape)

gr = df.groupby('gender')
print(len(gr))
# print(df['gender'].nunique())
# print(gr.size)
# print(gr['gender'].value_counts())
# print(gr.first())
# print(gr.groups)


# #retrive group from groupby object
print(gr.get_group('male'))


#methods on group by object
print(gr.max())
print(gr.min())
print(gr.sum())



print(gr.get_group('male').mean())

print(gr['math score'].sum())
####  grouping multiple column ###
#
# df1 = pd.read_csv('exams.csv')
# gr1 = df1.groupby('gender','lunch')
# print(gr1.sum())


#print(df.head())
# of common sector fall under each column the we can perform operation on that column

## .agg method(lef
print(gr.agg({'math'
              ' score':['sum','mean'],
       'reading score' : 'sum'}))

                                          # groupby iterating through rows nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

#merge Method

#1 Left join

import datetime as dt

print(pd.Timestamp('2015-03-11'))

print(pd.Timestamp('2021-03-04 08:35:15  PM'))


#CONVERTS TO PANDAS TIME STAMP

print(pd.Timestamp(dt.date(2019,1,11)))


#dates = ['2016/02/1','2017/02/11','2018/12/1']

#print(pd.DatetimeIndex(dates))

#
# drd = [dt.date('2011,02,11'),dt.date('2012,1,2') , dt.date('2011,2,9')]
# print(pd.DatetimeIndex(drd))

dates = [dt.date(2019,8,12),dt.date(2014,11,12),dt.date(2017,1,2)]
dtindex = pd.DatetimeIndex(dates)


values = [100,200,300]
print(pd.Series(data=values,index=dtindex))

print(pd.to_datetime('2019-09-11'))
print(pd.to_datetime(dt.date(2015,5,12)))
print(pd.to_datetime(dt.datetime(2014,3,4,2,3,4)))
print(pd.to_datetime(['2011-12-12','2018/2/4',2011,'December 6th,2011']))

times = pd.Series(['2014-4-2','2015-5-12','June 3rd,2018', 2012])
print(pd.to_datetime(times))


dtce =  pd.to_datetime([16534656324,364634265465])
print(dtce)

date12 = pd.date_range(start= '2011-1-2',end='2011-11-12',freq= 'MS')
print(date12)

daterange =(pd.date_range(start='2011-1-2',periods=25,freq='B')) # create 25 business days
print(daterange)

daterange1 = (pd.date_range(end='2011-1-2',periods=25,freq='B')) # print previous 25 days
print(daterange1)


#. .dt accesssor

bunch_dates = pd.date_range(start='2016-2-3',periods=11,freq='D')
print(bunch_dates)

s = pd.Series(bunch_dates)
print(s.dt.weekday_name)



import pandas_datareader.data as web
#
# company = 'MSFT'
# start ='2012-1-1'
# end = '2011-4-2'

#print(data.DataReader(name= 'Company',data_source = 'google',start=start,end=end))


#selecting from dataframe with a datetime index


#print(dt.datetime(before ='2011/2/1',after = '2011/9/10'))
#
#
# ndata = web.DataReader(name ='GOOG', data_source='google', start = dt.date(2000,1,2),end = dt.date(2019,2,12))
# print(ndata)


                                              ########         PANDAS DATE READER  NNNNNNNNNNNNNNNNNNNNNNN


### time delta object

timeA = pd.Timestamp('2012-2-1')
timeB = pd.Timestamp('2014-3-9')

print(timeB-timeA)
print(pd.Timedelta(weeks=3,days=8))


# timedeltas in datasets



#  PANEL OBJECT IN DATAFRAME






