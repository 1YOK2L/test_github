from random import *

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def get_time(self):
        return f"{self.hour:02d}:{self.minute:02d}"

class Calendar:
    def __init__(self, date, month, year):
        self.month = month
        self.year = year
        if date is None:
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                self.date = randint(1, 31)
            elif self.month in [4, 6, 9, 11]:
                self.date = randint(1, 30)
            elif self.month == 2:
                if self.year % 100 == 0 and self.year % 400 != 0:
                    self.date = randint(1, 28)
                elif self.year % 4 != 0:
                    self.date = randint(1, 28)
                else:
                    self.date = randint(1, 29)
        else:
            self.date = date
    
    def get_date(self):
        return f"{self.date:02d}/{self.month:02d}/{self.year:04d}"

class Watch(Clock, Calendar):
    def __init__(self, hour, minute, date = None, month = None, year = None):
        Clock.__init__(self, hour, minute)
        Calendar.__init__(self, date, month, year)

    def get_description(self):
        return f"{self.get_date()} {self.get_time()}"

clock = Clock(randint(0, 23), randint(0, 59))
calendar = Calendar(date = None, month = randint(1, 12), year = randint(1, 3000))
watch = Watch(16, 25, 4, 7, 2025)

print(clock.get_time())
print(calendar.get_date())
print(watch.get_description())