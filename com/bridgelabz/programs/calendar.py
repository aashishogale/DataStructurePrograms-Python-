from com.bridgelabz.utility.utility import Utility
class Calender:
    def run(self):
        month=int(input("enter month"))
        year=int(input("enter year"))
        Utility().Calenderprint(month,year)
        return



Calender().run()