class Date:
    '''class to represent a date'''

    def __init__(self,month,day,year):
        '''Date(month,day,year) -> Date'''
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        '''str(Date) -> str
        returns date in readable format'''
        # list of strings for the months
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul',
                  'Aug','Sep','Oct','Nov','Dec']
        output = months[self.month] + ' ' # month
        output += str(self.day) + ', '  # day
        output += str(self.year)
        return output

    def go_to_next_day(self):
        '''Date.go_to_next_day()
        advances the date to the next day'''
        # list with the days in the month
        daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        # check for leap year
        isLeapYear = self.year%4 
        if isLeapYear == 0:
            daysInMonth[2] += 1
        if self.day == daysInMonth[self.month]:
            if month == 12:
                self.month = 1
                self.day = 1
                self.year += 1
                return __str__(self)
            else:
                self.month += 1
                self.day = 1
                self.year = year
                return __str__(self)
        else:
            self.day += 1
            return __str__(self)