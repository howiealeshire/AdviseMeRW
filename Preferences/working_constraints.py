from constraint import *


'''
days = ['m','t','w','r','f']
#these are hard-coded for now
min_courses = int(p.min_courses)
max_courses = int(p.max_courses)
max_days = ['m','w','r']            # [1,1,1,1,1] # all days checked
min_days = ['m','t','w']  # what the user wants

# These are the times the user requested
hour_time_to = p.time_to[0]
hour_time_from = p.time_from[0]
minute_time_to = p.time_to[1]
minute_time_from = p.time_from[1]


max_time = int((str(hour_time_to).strip() + str(minute_time_to).strip()).strip()) #11 pm
min_time = int((str(hour_time_from).strip() + str(minute_time_from).strip()).strip())  #8 am

print(max_time)
print(min_time)
#sg = problem.getSolutions()
#
times = list(range(80,2400))
num_courses = list(range(min_courses,max_courses+1))

categories = p.cat
locations = p.loc
subjects = p.subjects
professors = p.prof
'''


'''
problem.addConstraint(lambda day,time,num_course,professor,subject,location:
                      day in max_days
                      and time <= max_time
                      and any(x in day for x in min_days)
                      and time >= min_time
                      and num_course <= max_courses
                      and num_course >= min_courses
                      and professor in professors
                      and subject in subjects
                      and location in locations
                      ,
                          ("day", "time","num_course","professor","subject","location"))
 


'''








def main(loc,cat,prof,days,time_to,time_from,time_interval,subjects,num_courses):

   print('location: ' + loc)
   print('categories: ' + cat)
   print('profs: ' + prof)
   print('days: ' + str(days))
   print('time_to: '  +  str(time_to))
   print('time_from: ' + str(time_from))
   print('time_interval: ' + str(time_interval))
   print('subjects: ' + str(subjects))
   print('num_courses: ' + str(num_courses))

   min_courses = num_courses[0]
   max_courses = num_courses[1]
   




   #turn time into fractional representation
   time_to = int((time_to[0] + (.01 * time_to[1])) * 100)
   time_from = int((time_from[0] + (.01 * time_from[1])) * 100)

   max_time = 2459
   min_time = 0
   time_range = list(range(min_time,max_time))
   problem = Problem()
   week_days = ['m','t','w','r','f']
   possible_days = []
   # might refractor this section, putting it into the PreferencesApp.py module,
   # that way this doesn't have to do all the parsing, cleaner and whatnot 
   #if days[0] == True:
   #   problem.addVariable("all_days",week_days)
   #else:
   if days[1] == True:
      possible_days += 'm'
   if days[2] == True:
      possible_days += 't'
   if days[3] == True:
      possible_days += 'w'
   if days[4] == True:
      possible_days += 'r'
   if days[5] == True:
      possible_days += 'f'
   
   '''

   #might be unnecessary, this section
   if possible_days == []:
      #this try except is so it can catch the duplicate variable exception. May check the constraint library and see if it has a function for this
      try:
         problem.addVariable("all_days",week_days)
      except ValueError:
         possible_days = week_days
         problem.addVariable("all_days",week_days)
   
   '''

         

   try:
      problem.addVariable("day", possible_days)
   except ValueError:
      possible_days = week_days
      problem.addVariable("day",possible_days)
      

   
#   problem.addVariable("time", times)
   problem.addVariable("num_course",num_courses)
   problem.addVariable("location",loc)
   problem.addVariable("professor",prof)
   problem.addVariable("category",cat)
   problem.addVariable("subject",subjects)

   

   problem.addConstraint(lambda day, num_course, professor, subject, location, category:
                            day in possible_days
                            #and time in time_range
                            and num_courses[1] <= max_courses
                            and num_courses[0] >= min_courses
                            and professor in prof
                            and subject in subjects
                            and location in loc
                         ,
                         ("day","num_course","professor","subject","location","category"))
                         

   p_iter = problem.getSolutionIter()
   
   
   print(next(p_iter))




    
if __name__ == "__main__": main()










