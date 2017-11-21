class Utility:

    def dayofweek(self, month, year):
        day = 1
        tempyear = year - (14 - month) // 12
        leap = tempyear + tempyear // 4 - tempyear // 100 + tempyear // 400
        tempmonth = month + 12 * ((14 - month) // 12) - 2
        d0 = int((day + leap + 31 * tempmonth // 12) % 7)
        return d0

    def Calenderprint(self,month,year):
        date=self.dayofweek(month,year)
        mnumber=1
        counter=0
        months=["january","february","march","april","may","june","july","august","september","october","november","december"]
        monthdays=[0 ,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if(self.isleap(year)):
            monthdays[2]=29
        print("=====================")
        print("S  M  T  W  T  F  S")
        print("=====================")
        for i in range(0,5):
            for j in range(0,7):
                if(counter<date):
                    print("   ",end="")
                    counter+=1
                elif(mnumber<=monthdays[month]):
                    print(mnumber,end="")
                    mnumber+=1
                    if(mnumber<11):
                        print("  ",end="")
                    else:
                        print(" ",end="")

            print("\n")
        return

    def isleap(self,year):
        if len(str(year)) != 4:

            return ("please enter correct year")
        elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:

            return True
        else:

            return False

