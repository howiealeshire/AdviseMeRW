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

   print('location: ' + str(loc))
   print('categories: ' + str(cat))
   print('profs: ' + str(prof))
   print('days: ' + str(days))
   print('time_to: '  +  str(time_to))
   print('time_from: ' + str(time_from))
   print('time_interval: ' + str(time_interval))
   print('subjects: ' + str(subjects))
   print('num_courses: ' + str(num_courses))

   min_courses = num_courses[0]
   max_courses = num_courses[1]
   
   course_range = list(range(min_courses,max_courses))



   #turn time into fractional representation
   time_to = int((time_to[0] + (.01 * time_to[1])) * 100)
   time_from = int((time_from[0] + (.01 * time_from[1])) * 100)

   max_time = 2359
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


   list_profs = ["Dr. Howie", "Dr. Aleshire", "Dr. Howard"]

   

   try:
      problem.addVariable("day", possible_days)
   except ValueError:
      possible_days = week_days
      problem.addVariable("day",possible_days)
      


   problem.addVariable("time_prime", time_range)
   try:
      problem.addVariable("num_courses",course_range)
   except ValueError:
      course_range = list(range(0,8)) #course range is hardcoded for now, will plug field from file later
      problem.addVariable("num_courses",course_range)
      
   
   loc_possible = ["Computer Science", "Mathematics"]

   if loc != []:
      problem.addVariable("location",loc)
   
   if prof != []:
      problem.addVariable("professor",list_profs)
   
   
 #  cat = ["WI","GLT","SI"]

   if cat != []:
      problem.addVariable("category",cat)

  # subjects = ["Computer Science", "Mathematics"] 

   if subjects != []:
      problem.addVariable("subject",subjects)


   
   
   prof_prime = prof 
   subj_prime = subjects
   cat_prime = cat
   loc_prime = loc
   
   



   print(subjects)

   #perhaps something should be done about the ValueError that occurs when the range of courses is between 0 and 0
   #try except later, perhaps
   i = 0
   len_prof = len(prof_prime)
   len_subj = len(subj_prime)
   len_cat = len(cat_prime)
   len_loc = len(loc_prime)


   problem.addConstraint(lambda day, time_prime,num_courses:
                               day in possible_days
                               and time_from <= time_prime
                               and time_to >= time_prime
                               and min_courses <= num_courses
                               and max_courses >= num_courses
                             ,
                            ("day","time_prime","num_courses"))





   p_iter = problem.getSolutionIter()
   
   i = 0
   while i <= 40:
      print(next(p_iter,None))      
      i += 1

   #print(next(p_iter))
   #print(next(p_iter))
   #print(next(p_iter)
   #print(problem.getSolutions())



    
if __name__ == "__main__": main()










