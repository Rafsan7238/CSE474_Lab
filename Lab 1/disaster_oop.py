# import necessary libraries
import math
import datetime

# create parent Disaster class
class Disaster:

    # set default attributes according to specific data types
    casualties = 0
    injuries = 0
    list_of_casualties = []
    list_of_injuries = []
    financial_loss = 0
    impact_factor = math.log(injuries + 1) + math.sqrt(casualties) + (1.12 ** (financial_loss / 100))

    '''
    Initialise with datetime object and location.

    If date_time is not given in the constructor, set the current date and time. If location is
    missing, assign “Bangladesh"
    '''
    def __init__(self, date_time = datetime.datetime.now(), location = "Bangladesh"):
        self.date_time = date_time
        self.location = location

    # return all attributes
    def __str__(self):
        string_return = 'date_time: ' + str(self.date_time) + ', location: ' + str(self.location) + \
        ', casualties: ' + str(self.casualties)+ ', injuries: ' + str(self.injuries)+ ', financial_loss: ' \
        + str(self.financial_loss)+ ', impact_factor: ' + str(self.impact_factor)+ ', list_of_casualties: ' \
        + str(self.list_of_casualties)+ ', list_of_injuries: ' + str(self.list_of_injuries)

        return string_return

    '''
    Update injuries and/or list_of_injuries. 
    If only an integer n is given as the parameter, add it to the injuries, and append n
    dictionary items in the list with {“name” : “unknown”, “age” : “unknown”, “NID_no” : “unknown”}. 

    If a list is given as a parameter, append it to the corresponding list, and update the
    number of injuries. 

    If both a number and a list are given as parameters, both the tasks will be performed.
    '''
    def _update_injuries(self, n = 0, injury_list = []):

        if injury_list != []:
            self.injuries += len(injury_list)
            self.list_of_injuries += injury_list

        if n != 0:
            self.injuries += n

            for i in range(n):
                self.list_of_injuries.append({'name' : 'unknown', 'age' : 'unknown', 'NID_no' : 'unknown'})

    '''
    Update casualties and/or list_of_casualties. 
    If only an integer n is given as the parameter, add it to the casualties, and append n
    dictionary items in the list with {“name” : “unknown”, “age” : “unknown”, “NID_no” : “unknown”}. 

    If a list is given as a parameter, append it to the corresponding list, and update the
    number of casualties. 

    If both a number and a list are given as parameters, both the tasks will be performed.
    '''
    def _update_casualties(self, n = 0, casualty_list = []):
        if casualty_list != []:
            self.casualties += len(casualty_list)
            self.list_of_casualties += casualty_list

        if n != 0:
            self.casualties += n

            for i in range(n):
                self.list_of_casualties.append({'name' : 'unknown', 'age' : 'unknown', 'NID_no' : 'unknown'})


# inherit Earthquake class from Disaster
class Earthquake(Disaster):

    '''
    Call the super's init method to set date_time and location. 
    It has its own source and seismic_scale parameters.
    '''
    def __init__(self, date_time = datetime.datetime.now(), location = "Bangladesh", source = "", seismic_scale = 0.0):
        self.source = source
        self.seismic_scale = seismic_scale
        super().__init__(date_time, location)

    # return all attributes including super's
    def __str__(self):
        string_return = super().__str__()
        string_return = string_return + ', source: ' + str(self.source) + ', seismic_scale: ' + str(self.seismic_scale)
        return string_return

# inherit Flood class from Disaster
class Flood(Disaster):

    '''
    Call the super's init method to set date_time and location. 
    It has its own water_level parameter.
    '''
    def __init__(self, date_time = datetime.datetime.now(), location = "Bangladesh", water_level = 0.0):
        self.water_level = water_level
        super().__init__(date_time, location)

    # return all attributes including super's
    def __str__(self):
        string_return = super().__str__()
        string_return = string_return + ', water_level: ' + str(self.water_level)
        return string_return

# inherit Cyclone class from Disaster
class Cyclone(Disaster):

    '''
    Call the super's init method to set date_time and location. 
    It has its own source and water_level parameters.
    '''
    def __init__(self, date_time = datetime.datetime.now(), location = "Bangladesh", source = "", water_level = 0.0):
        self.source = source
        self.water_level = water_level
        super().__init__(date_time, location)

    # return all attributes including super's
    def __str__(self):
        string_return = super().__str__()
        string_return = string_return + ', source: ' + str(self.source) + ', water_level: ' + str(self.water_level)
        return string_return

# inherit Drought class from Disaster
class Drought(Disaster):

    '''
    Call the super's init method to set date_time and location. 
    It has its own list_of_affected_crops parameter.
    '''
    def __init__(self, date_time = datetime.datetime.now(), location = "Bangladesh", list_of_affected_crops = []):
        self.list_of_affected_crops = list_of_affected_crops
        super().__init__(date_time, location)

    # return all attributes including super's
    def __str__(self):
        string_return = super().__str__()
        string_return = string_return + ', list_of_affected_crops: ' + str(self.list_of_affected_crops)
        return string_return


'''
If _merge(event1, event2) is called, their types, date_time,
and location will be compared. If the type matches,their location attributes match, and their dates
match (not time), create a new object by merging their details. The location should remain constant.
Merge the lists of injuries/casualties and update their numbers accordingly. Finally, delete the objects
event1 and event2, and return the new object.

The rest attributes are merged into lists.
'''
def _merge(event1, event2):

    # date() method of a datetime object returns the date information of the object
    if type(event1) == type(event2) and event1.date_time.date() == event2.date_time.date() and event1.location == event2.location:
        
        # if we have an object of a class called A in main, its type becomes '__main__.A'
        # keep the original datetime and location
        if type(event1) == '__main__.Disaster':
            event3 = Disaster(event1.date_time, event1.location)

        elif type(event1) == '__main__.Earthquake':
            event3 = Earthquake(event1.date_time, event1.location, [event1.source, event2.source], [event1.seismic_scale, event2.seismic_scale])

        elif type(event1) == '__main__.Flood':
            event3 = Flood(event1.date_time, event1.location, [event1.water_level, event2.water_level])

        elif type(event1) == '__main__.Cyclone':
            event3 = Cyclone(event1.date_time, event1.location, [event1.source, event2.source], [event1.water_level, event2.water_level])

        elif type(event1) == '__main__.Drought':
            event3 = Drought(event1.date_time, event1.location, event1.list_of_affected_crops + event2.list_of_affected_crops)

        # update the list and numbers of injuries and casualties by adding them
        event3.casualties = event1.casualties + event2.casualties
        event3.injuries = event1.injuries + event2.injuries
        event3.list_of_injuries = event1.list_of_injuries + event2.list_of_injuries
        event3.list_of_casualties = event1.list_of_casualties + event2.list_of_casualties
        event3.financial_loss = event1.financial_loss + event2.financial_loss
        event3.impact_factor = math.log(event3.injuries + 1) + math.sqrt(event3.casualties) + (1.12 ** (event3.financial_loss / 100))

        # delete the old events and return the new event
        del event1
        del event2
        return event3
