import pandas as pd
import math
import numpy as np

#with this file, i guess we'll make it so that it is the one that doesn't require prereqs (although it currently parses them). Still considering organization.
#perhaps once this file is parsed completely, we could pipe it to a class that takes the data, checks it against courses that have already been taken, eliminates
#courses that can't be taken bc prereqs haven't been taken yet, then pipe this final output into constraints.py (the current class, parseCSV, will have already taken care of formatting issues and whatnot)

#credit goes to StackOverflow user @SunilT for pandas code (not listed) to keep only certain columns from csv file:
# https://stackoverflow.com/questions/7588934/deleting-columns-in-a-csv-with-python

#later replace hardcoded with user/admin input file
df=pd.read_csv('newFile.csv')


#print(df)

keep_col = ['CRN','Course','Title','SH','Instructor','Meeting Dates', 'Days','Time','Categories','Seats','Limit','Enroll','Subject','Prerequisites']

crn = df['CRN']
course = df['Course']
title = df['Title']
sh = df['SH']
instructor = df['Instructor']
meeting_dates = df['Meeting Dates']
days = df['Days']
time = df['Time']
categories = df['Categories']
seats = df['Seats']
limit = df['Limit']
enroll = df['Enroll']
subject = df['Subject']
prerequisites = df['Prerequisites']

categories = df['Categories']

crn = df['CRN']
course = df['Course']
title = df['Title']
sh = df['SH']
instructor = df['Instructor']
meeting_dates = df['Meeting Dates']
days = df['Days']
time = df['Time']
categories = df['Categories']
seats = df['Seats']
limit = df['Limit']
enroll = df['Enroll']
subject = df['Subject']
prerequisites = df['Prerequisites']

categories = df['Categories']

def main():
    df=pd.read_csv('newFile.csv')


    #print(df)

    keep_col = ['CRN','Course','Title','SH','Instructor','Meeting Dates', 'Days','Time','Categories','Seats','Limit','Enroll','Subject','Prerequisites']


    nan= float('nan')
    s = ['CSC250', 'CSC230']

    #s = pd.Series(courses_taken)
    
    for i, row in df.iterrows():
        pre_req = str(row['Prerequisites'])

        pre_req = pre_req.strip('[')
        pre_req = pre_req.strip(']')
        pr = pre_req.split(',')
        for x in pr:
            if x not in s and pd.isnull(x) == False:
                df.drop(df.index[i])


    print(df)
        
        
            
            
if __name__ == "__main__":
    main()


#new_df = df[keep_col]

#new_df.to_csv("newFile.csv", index=False)

#print(df[0])

