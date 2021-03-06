#~ = marked for deletion, just checking if code still works

import sys
from constraint import *
sys.path.insert(0, '/Users/howard/AdviseMeRW/Recommendations/Recommendations')
import parseCSV

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

   preferred_time_range = list(range(time_from,time_to))

   
   problem = Problem()
   week_days = ['m','t','w','r','f']
   possible_days = []



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
   

   try:
      problem.addVariable("day", possible_days)
   except ValueError:
      possible_days = week_days
      problem.addVariable("day",possible_days)
      


   problem.addVariable("time_prime_max", preferred_time_range)
   problem.addVariable("time_prime_min", preferred_time_range)
   try:
      problem.addVariable("num_courses",course_range)
   except ValueError:
      course_range = list(range(0,8)) #course range is hardcoded for now (to prevent default value of []), will plug field from file later maybe
      problem.addVariable("num_courses",course_range)
      
   

   if loc != []:
      problem.addVariable("location",loc)
   
   if prof != []:
      problem.addVariable("professor",prof)

   
   

   if cat != []:
      problem.addVariable("category",cat)


   if subjects != []:
      problem.addVariable("subject",subjects)


   
   


   problem.addConstraint(lambda day, num_courses,time_prime_min,time_prime_max:
                               day in possible_days
                               and time_from <= time_prime_min
                               and time_to >= time_prime_max
                               and min_courses <= num_courses
                               and max_courses >= num_courses
                             ,
                            ("day","num_courses","time_prime_min","time_prime_max"))




   
   p_iter = problem.getSolutionIter()
  # print(ppp)

   solution_list = []
   i = 0
   while i <= 4:
      solution_list.append(next(p_iter,None))
      i += 1

   print("solution list: ") 
   print(solution_list)
   print("end solution list ")
   final_course_list = parseCSV.main(solution_list)
   #print(final_course_list)
   return final_course_list
   #print(next(p_iter))
   #print(next(p_iter))
   #print(next(p_iter)
   #print(problem.getSolutions())
   

    
if __name__ == "__main__": main()










