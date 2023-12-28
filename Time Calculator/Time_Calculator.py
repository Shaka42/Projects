class Time:
    def __init__(self,hour,minute,area,day=None):
        self.hour = hour
        self.minute = minute
        self.area = area
        self.day = day
        self.count = 1
        self.days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    def normal(self):
        if self.day is not None:
            self.day = str(self.day).capitalize()
            if self.count > 1:
                print("Return:", str(self.hour) + ':' + str(self.minute), self.area,
                      '( ' + str(self.count) + ' days later)')
            else:
                print("Return:", str(self.hour) + ':' + str(self.minute), self.area,self.day)
        elif self.count > 1:
            print("Return:", str(self.hour) + ':' + str(self.minute), self.area,'( '+str(self.count)+' days later)')
        else:
            print("Return:",str(self.hour)+':'+str(self.minute),self.area)

    def change(self):
        if self.day is not None:
            self.day = str(self.day).capitalize()
            if self.area == 'AM':
                self.area = 'PM'
                print("Return:", str(self.hour) + ':' + str(self.minute), self.area,self.day)
                quit()
        elif self.area == 'AM':
            self.area = 'PM'
            print("Return:",str(self.hour)+':'+str(self.minute),self.area)
            quit()
    def changeday(self):
        if self.day is not None:
            self.day = self.day.capitalize()
            a = self.days.index(self.day) + 1
            self.day = self.days[a]
            if self.area == 'PM':
                self.area = 'AM'
                print("Return:", str(self.hour) + ':' + str(self.minute), self.area, self.day)
        if self.area == 'PM':
            self.area = 'AM'
            print("Return:",str(self.hour)+':'+str(self.minute),self.area,'(nextday)')

    def changes_day2(self):
        if self.day is not None:
            self.day = self.day.capitalize()
            if self.count > 1:
                if self.area == 'PM':
                    self.area = 'AM'
                    print("Return:", str(self.hour) + ':' + str(self.minute), self.area,self.day,
                          '( ' + str(self.count) + ' days later)')
                    quit()
                if self.area == 'AM':
                    self.area = 'PM'
                    print("Return:", str(self.hour) + ':' + str(self.minute), self.area,self.day,
                          '( ' + str(self.count) + ' days later)')
                    quit()
        if self.count > 1:
            if self.area == 'PM':
                self.area ='AM'
                print("Return:",str(self.hour)+':'+str(self.minute),self.area,'( '+ str(self.count)+' days later)')
                quit()
            if self.area == 'AM':
                self.area = 'PM'
                print("Return:", str(self.hour) + ':' + str(self.minute), self.area, '( ' + str(self.count) + ' days later)')
    def days_later(self):
        self.count = 1
        if self.day is not None:
            self.day = self.day.capitalize()
            while self.hour > 24:
                self.hour = self.hour - 24
                self.count += 1
                continue
            x = self.days.index(self.day) + self.count
            if x  > len(self.days):
                while x > len(self.days):
                    x = x - len(self.days)
                    continue
                self.day = self.days[x]
            else:
                self.day = self.days[x]
        else:
            while self.hour > 24:
                self.hour = self.hour - 24
                self.count += 1
                continue

def add_time(a,b,c=None):
    f = a.split(":")
    z = f[1].split(' ')
    z.insert(0, a[0])
    f = b.split(':')
    k = f[1].split(' ')
    k.insert(0, b[0])
    if 2 > 1:
        hour = int(z[0]) + int(k[0])
        minute = int(z[1]) + int(k[1])
        m = Time(hour,minute,z[2],c)
        if m.minute < 60:
            m.minute = str(m.minute).zfill(2)
            if m.hour < 12:
                m.normal()
            elif m.hour > 24:
                m.days_later()
                if m.hour == 12:
                    m.changes_day2()
                if m.hour < 12:
                    m.normal()
                if m.hour > 12:
                    m.hour = m.hour - 12
                    m.hour = str(m.hour)
                    if int(m.hour) < 12:
                        m.changes_day2()

            elif m.hour >= 12:
                if m.hour == 12:
                    m.change()
                    m.changeday()
                else:
                    m.hour = m.hour - 12
                    m.hour = str(m.hour)
                    if int(m.hour) < 12:
                        m.change()
                        m.changeday()

        elif m.minute >= 60:
            m.minute = m.minute - 60
            m.minute = str(m.minute).zfill(2)
            m.add_hour = 1
            if m.hour > 24:
                m.hour = m.hour + 1
                m.days_later()
                if m.hour < 12:
                    m.normal()
                if m.hour >= 12:
                    if m.hour == 12:
                        m.changes_day2()
                    elif m.hour > 12:
                        m.hour = m.hour - 12
                        m.hour = str(m.hour)
                        if int(m.hour) < 12:
                            m.changes_day2()
            elif m.hour < 12:
                m.hour = m.add_hour + m.hour
                m.hour = str(m.hour)
                if int(m.hour) < 12:
                    m.change()
                    m.changeday()
                if int(m.hour) == 12:
                    m.change()
                    m.changeday()
            elif m.hour >= 12:
                m.hour = m.add_hour + m.hour
                m.hour = m.hour - 12
                if m.hour == 12:
                    m.change()
                    m.changeday()
                if int(m.hour) < 12:
                    m.change()
                    m.changeday()



add_time('9:00 PM','3:10','Thursday')
