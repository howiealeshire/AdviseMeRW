from pprint import pprint



class Preferences(object):
    def __init__ (self,loc,cat,prof,days,time_to,time_from,time_interval,subjects,num_courses):
        
        self.loc = loc
        self.cat = cat
        self.prof = prof
        self.days = days
        self.time_to = time_to
        self.time_from = time_from
        self.time_interval = time_interval
        self.subjects = subjects
        self.num_courses = num_courses
        self.min_courses = self.num_courses[0]
        self.max_courses = self.num_courses[1]
        


def main(loc,cat,prof,days,time_to,time_from,time_interval,subjects,num_courses):

        p = Preferences(loc,cat,prof,days,time_to,time_from,time_interval,subjects,num_courses)
        pprint(vars(p))
        return p


if __name__ == "__main__":
    main()

