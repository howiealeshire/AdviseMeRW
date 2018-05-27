from constraint import *
from collections import deque
import Preferences


p = Preferences.main()

#necessary declaration for constraints lib
problem = Problem()


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


"""  Tomorrow: instantiate the constraints class in preferences class, so that way the state can be threaded through it """
