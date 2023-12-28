class Time_calculator:
    add_hour = 1
    count = 1
    def __init__(self,hour,minute,area):
        self.hour = hour
        self.minute = minute
        self.area = area
        self.days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    def add_time1(self):
        print()
    def add_time2(self):
        self.count = 1
        while self.hour > 24:
            self.hour = self.hour - 24
            self.count += 1
            continue
        print(self.hour, self.count)
        if self.hour > 12:
            self.hour =self.hour - 12
            #self.hour = self.hour + self.add_hour
            hour = str(self.hour).zfill(2)
            print(hour, self.minute)
        else:
            hour = str(self.hour).zfill(2)
            print(hour, self.minute)
    def changewithdayslater(self):
        if self.area == 'AM':
            self.area = 'PM'
            print("Return:", str(self.hour) + ':' +str(self.minute), self.area, '(',str(self.count), 'days later )')
        if self.area == 'PM':
            self.area = 'AM'
            print("Return:", str(self.hour) + ':' + self.minute, self.area, '(',str(self.count), 'days later )')
    def nextday(self):
        if self.area == 'PM':
            self.area = 'AM'
            print("Return:",str(self.hour)+':'+str(self.minute),self.area,'(next day)')
    def change(self):
        for i in  self.count:
            if self.area == 'PM':
                self.area = 'AM'
            if self.area == 'PM':
                self.area = 'AM'
def add_time(a,b, c = None):
    a = a.split(" ")
    b= b .split(" ")
    if c is None:
        hour = int(a[0]) + int(b[0])
        minute = int(a[2]) + int(b[2])
        print(hour, minute)
        m = Time_calculator(hour,minute,a[3])
        if m.minute < 60:
            m.minute = str(m.minute).zfill(2)
            if m.hour > 24:
                m.add_time2()
                if m.count > 1:
                    m.changewithdayslater()
                if m.count == 1:
                    m.nextday()
            if m.hour > 12:
                m.add_time2()
                m.nextday()
            #if m.hour < 12:
        elif m.minute >= 60:
            m.minute = m.minute - 60
            m.minute = str(m.minute).zfill(2)



add_time('6 : 30 PM','205 : 12')















