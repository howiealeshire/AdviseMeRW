#an idea i have is to either populate a new pandas dataframe incrementally. or, if that doesn't work, a list of dictionaries instead
import pandas as pd
import math
import numpy as np

#with this file, i guess we'll make it so that it is the one that doesn't require prereqs (although it currently parses them). Still considering organization.
#perhaps once this file is parsed completely, we could pipe it to a class that takes the data, checks it against courses that have already been taken, eliminates
#courses that can't be taken bc prereqs haven't been taken yet, then pipe this final output into constraints.py (the current class, parseCSV, will have already taken care of formatting issues and whatnot)

#credit goes to StackOverflow user @SunilT for pandas code (not listed) to keep only certain columns from csv file:
# https://stackoverflow.com/questions/7588934/deleting-columns-in-a-csv-with-python

#later replace hardcoded with user/admin input file


def read_courses_taken():
    courses_taken = open('/Users/howard/AdviseMeRW/Recommendations/Recommendations/taken_courses.txt','r')
    course_list = []
    for course in courses_taken:
        course_list.append(course.rstrip().replace(' ',''))
        
        print(course)
    courses_taken.close()
    return course_list





#when ready, main will take argument 's', which will be the courses the user has already taken. Considering calling it form
def main(preferences):
    pre_reqs = read_courses_taken()
    for p in pre_reqs:
        print(p)
    df=pd.read_csv('/Users/howard/AdviseMeRW/Recommendations/Recommendations/newFile.csv')
    df_dict = df.to_dict('records')
    

    keep_col = ['CRN','Course','Title','SH','Instructor','Meeting Dates', 'Days','Time','Categories','Seats','Limit','Enroll','Subject','Prerequisites']


    nan = float('nan')

    

            
    print("*****")
    #s = pd.Series(courses_taken)

    #basically, go through, check if the student has the necessary prerequisites. If not, remove the course from the potential offerings
    dq = []

    #this, in theory, works. It removes the dict from the list if the student doesn't have the necessary prereqs
    print(len(df_dict))
    for i, pre in enumerate(d['Prerequisites'] for d in df_dict):
        if type(pre) is not float:
            #code to parse file correctly, might write to file for future reference
            #also need to parse things like 'senior' and such
            pre = pre.strip('[')
            pre = pre.strip(']')
            pre = pre.replace('\'','')
            pre = pre.replace(' ','')
            if pre not in pre_reqs:
                dq.append(df_dict.pop(i))

    

    
    print(len(df_dict))               
    #print(dq)
        
    #for i, row in enumerate(dict_df):
#        print(i,row)
        
        #flag = False
        #pre_req = str(row['Prerequisites'])
        
        #pre_req = pre_req.strip('[')
        #pre_req = pre_req.strip(']')
        #pre_req = pre_req.replace('\'','')
        #pre_req = pre_req.replace(' ','')

#        pr = pre_req.split(',')
#        print(i)
        #dict_df.pop(i)
        #for x in pr:
            #if x not in pre_reqs and pd.notnull(x) == True:
                
                
                # print(x)
                #flag = True
        #if flag == True:
#            df.drop(df.index[i],inplace=True)

    

    #print(df)
    #main (or perhaps another method) will return a list of dictionaries. Each dictionary will be a course object. Maybe will transform into it's own object?








    
        
            
            
if __name__ == "__main__":
    main()





#new_df = df[keep_col]

#new_df.to_csv("newFile.csv", index=False)

#print(df[0])


