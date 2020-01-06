import pandas as pd


# ###########    PANDAS   SERIES ########


p1=pd.read_csv('example.csv',squeeze=True)

# HEAD AND TAIL

#
# print(p1.head()) # PRINT FIRST 5 VALUES
# print(p1.head(3)) # PRINT FIRST 3 VALUES
# print(p1.tail())# PRINT LAST 5 VALUES
# print(p1.tail(3)) # PRINT LAST 3 VALUES


#                # MATH OPERATION ON PANDAS SERIES
#
#                   sum method
# print(p1.sum()) # returns sum of all values in individual columns
#
#
#                       COUNT method
# print(p1.count()) # returns number of rows in each columns
#
#                       MEDIAN method
#print(p1.median()) # returns median values in each column

#                     MIN method
#print(p1.min())#   return minimun values in each column



#                    MAX Method
#print(p1.max())# return maximum values in each column


#                  STD Method
#print(p1.std())  # RETURN STANDARD DEVIATION  of each column

#                       Mode Method
#print(p1.mode()) # return most repeated value in each columm


                                                                       #VALUE COUNT METHOD   1
                                                                      #print(p1.value_counts())  2

                                                                      # Map  3
                                                                      #apply   4
                                                                    #idxmin and idxmax values remaining  5



## Sort Value Method ##
#
# print(p1.sort_values(by=['iso3'],ascending=True).head(10))
#
# print(p1.sort_values(by=['iso3'],ascending=True).tail(10))
#
#
# print(p1.sort_values(by=['iso3'],ascending= False).head(10))
#
#
#
# #shape Method
#
# print(p1.shape)


#IN PLACE PARAMETER

#abc = p1.sort_values(by= ['e_prevtx_eligible'],ascending= True)
#abc = p1.sort_values(by= ['iso3'])
#print(abc.head(3))




