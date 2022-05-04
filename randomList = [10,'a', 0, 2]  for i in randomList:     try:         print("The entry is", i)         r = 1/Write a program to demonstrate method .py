class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def print(self):
        print("Super Class Method Called",self.hr,":",self.min,":",self.sec)

class Clock(Time):
    def __init__(self,hr,min,sec):
        Time.__init__(self, hr, min, sec)
    def print(self):
        super().print()
        if self.hr<12:
            self.str="AM"
        else:
            self.str="PM"
        print("Sub Class Method Called",self.hr,":",self.min,":",self.sec,self.str)

c=Clock(12,40,30)
c.print()
