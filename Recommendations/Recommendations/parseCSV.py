import pandas as pd
import math
import numpy as np
import sys
import copy





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

#probably should use generators in this expression, so that way it's not ridiculously inefficient
#{'day': 'm', 'num_courses': 2, 'time_prime': 200, 'category': 'WI', 'location': 'Sullivan', 'subject': 'Computer Science', 'professor': 'Dr. Howie
    days = []
    for (i,day) in enumerate(d['day'] for d in preferences): 
        #print(i,num)
        days.append(day)
    num_courses = []
    for (i, num) in enumerate(d['num_courses'] for d in preferences): 
        #print(i,num)
        num_courses.append(num)

    min_times = []
    for (i, min_time) in enumerate(d['time_prime_min'] for d in preferences):
        #print(i,num)
        min_time = float(min_time)
        min_times.append(min_time)

    max_times = []
    for (i, max_time) in enumerate(d['time_prime_max'] for d in preferences):
        #print(i,num)
        max_time = float(max_time)
        max_times.append(max_time)



    

    category = []
    for (i, cat) in enumerate(d['category'] for d in preferences):
        category.append(cat)
        #print(i,num)

    location = []
    for (i, loc) in enumerate(d['location'] for d in preferences):
        location.append(loc)
        #print(i,num)

    subjects = []
    for (i, subj) in enumerate(d['subject'] for d in preferences):
        subjects.append(subj)
        #print(i,num)

    professors = set()
    for (i,prof) in enumerate(d['professor'] for d in preferences):
        if type(prof) != float:
            prof = prof.rstrip().replace(' ','')
            professors.add(prof)
    print("ya know")
    for p in professors:
        print(p)
    print("yeah")
    
        #print(i,num)
    print("professor list begin: ")
    print(professors)
    print("professor list end: ")
    #print(preferences)
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
    test_it = 0

    ''' pretty sure pre works '''
    
    for i, pre in enumerate(d['Prerequisites'] for d in df_dict):
         if type(pre) is not float:
            #code to parse file correctly, might write to file for future reference
            #also need to parse things like 'senior' and such
            pre = pre.strip('[')
            pre = pre.strip(']')
            pre = pre.replace('\'','')
            pre = pre.replace(' ','')
            if test_it == 0:
                print("pre: ")
                print(pre)
                print("end pre.")
                test_it += 1
            if pre not in pre_reqs:
                dq.append(df_dict.pop(i))

    

    #for i, course in enumerate(d['Course'] for d in df_dict):
        #get rid of section number from course, might later parse into its own category
#        course = course[:-3]
#        if course not in  

    test_it = 0

    '''pretty sure prof also works too '''

    copy_df_dict = copy.deepcopy(df_dict)
    for d in df_dict:
        for k,v in d.items():
            if k == 'Instructor':
                if type(v) != float:
                    v = v.rstrip().replace(' ','')

                if v not in professors:
                    copy_df_dict.remove(d)
                           
    print(copy_df_dict)

    
    
    for i, prof in enumerate(d['Instructor'] for d in df_dict):
        if type(prof) != float:
            prof = prof.rstrip().replace(' ','')
            if prof not in  professors:
                #print("profs not in professors: ")
                #print(prof)
                if test_it == 0:
                    print("pre2: ")
                    print(prof)
                    print("end pre2.")
                    test_it += 1
                dq.append(df_dict['Instructor'].remove(prof))
            else:
                print("strange profs who are in list: ")
                print(prof)
                print("end strange profs who are in list and who shouldn't be. ")
    
                
            


    ccopy_df_dict = copy.deepcopy(copy_df_dict)
    
    for d in copy_df_dict:
        for k,v in d.items():
            if k == 'Time':
                if type(v) != float and v != 'nan':
                    v = v.split('-')
                    time_from = v[0]
                    time_to = v[1]
                
                    for (x,y) in zip(time_from,time_to):
                        x = float(x)
                        y = float(y)
                        if (x,y) not in zip(min_times,max_times) or x < min_time: and y > max_time:
                            try:
                                time_from_f = float(time_from)
                                time_to_f = float(time_to)
                                x_f = float(x)
                                
                                ccopy_df_dict.remove(d)
                            except ValueError:
                                pass
                        
                        elif v == 'nan':
                            ccopy_df_dict.remove(d)
                        elif x >= min_time or y <= max_time:
                            break

                        else:
                            ccopy_df_dict.remove(d)
    print(ccopy_df_dict)
    

    #days
    cccopy_df_dict = copy.deepcopy(ccopy_df_dict)
    for d in ccopy_df_dict:
        for k,v in d.items():
            if k == 'Days':
                if type(v) != float and v != 'nan':
                    v = v.replace(" ","")
                    v = v.lower()
                    if v[1] != days[0]:
                        try:
                            cccopy_df_dict.remove(d)
                        except ValueError:
                            pass
                            
 
                
                elif v == 'nan':
                    cccopy_df_dict.remove(d)
                else:
                    cccopy_df_dict.remove(d)
    print(cccopy_df_dict)
 
    

                
    


    '''

    
    for i, day in enumerate(d['Days'] for d in df_dict):
        if type(day) is not float:
            day = day.replace(" ","")
            day = day.lower()
        
            for x in day:
                if x not in days:
                    df_dict.pop()

    '''

    '''
    for i, time in enumerate(d['Time'] for d in df_dict):
        if type(time) is not float:
            time = time.split('-')
            time_from = time[0]
            time_to = time[1]
            for (x,y) in zip(time_from,time_to):
                if (x,y) not in zip(min_times,max_times):
                    df_dict.pop()
    '''





    ccccopy_df_dict = copy.deepcopy(cccopy_df_dict)
    for d in cccopy_df_dict:
        for k,v in d.items():
            if k == 'Categories':
                if type(v) != float and v != 'nan':
                    v = v.replace(" ","")
                    v = v.strip('.')
                    v = v.split('.')
                    for x in v:
                        if x not in category:
                            try:
                                ccccopy_df_dict.remove(d)
                            except ValueError:
                                pass
                elif v == 'nan':
                    ccccopy_df_dict.remove(d)
                else:
                    ccccopy_df_dict.remove(d)
    print(ccccopy_df_dict)



    cccccopy_df_dict = copy.deepcopy(ccccopy_df_dict)
    for d in ccccopy_df_dict:
        for k,v in d.items():
            if k == 'Subjects':
                if type(v) != float and v != 'nan':
                    for x in v:
                        if x not in category:
                            try:
                                cccccopy_df_dict.remove(d)
                            except ValueError:
                                pass
                elif v == 'nan':
                    cccccopy_df_dict.remove(d)
                else:
                    cccccopy_df_dict.remove(d)
    print(cccccopy_df_dict)



    
        
'''            
    for i, cat in enumerate(d['Categories'] for d in df_dict):
        if type(cat) is not float:
            cat = cat.strip('.')
            cat = cat.split('.')
            for x in cat:
                if x not in category:
                    df_dict.pop()

'''




    '''
    for i, subj in enumerate(d['Subject'] for d in df_dict):
        subj = subj.title()
        if subj not in subjects:
            df_dict.pop(i)
    '''

    
'''
    new_time = []
    new_dict = []

    #print("start df_dict")
    #print(df_dict)
   # print("end df_dict")
   
    # this is to prevent duplicate times 
    for i, time in enumerate(d['Time'] for d in df_dict):
        if type(time) is not float:
            time = time.strip()
            time = time.split('-')
            if time not in new_time:
                new_dict.append(df_dict[i])
                new_time.append(time)
    

    
    '''
    



    

 #   for i, prof in enumerate(d['Instructor'] for d in df_dict):
#        if prof in 

    

    

    

    print('len dict')
    print(len(df_dict))
    
    print('len new_Dict')
    print(len(new_time))

    return new_dict
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

    
    #print(df_dict)
 #   sched = Schedule.main()
 #   sched.set_courses(df_dict)



    
        
            
            
if __name__ == "__main__":
    main()





#new_df = df[keep_col]

#new_df.to_csv("newFile.csv", index=False)

#print(df[0])


