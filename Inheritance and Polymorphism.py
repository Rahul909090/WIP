# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:43:52 2024

@author: noodl
"""
#Question 1
class Course:
    def __init__(self):
        self.number = input("Enter the Course Number: ")
        self.title = input("Enter the Course Title: ")
        
    def setNum(self, num):
        self.number = num
    def setTitle(self, title):
        self.title = title
    def getNum(self):
        return self.number
    def getTitle(self):
        return self.title
    
class OfferedCourse(Course):
    def __init__(self, number, title, instructor_name, course_location, class_time):
        super().__init__()
        self.setNum(number)
        self.setTitle(title)
        self.instructor_name = instructor_name
        self.course_location = course_location
        self.class_time = class_time
        
    def setInstructor(self, name):
        self.instructor_name = name
    def setLocation(self, loc):
        self.course_location = loc
    def setTime(self, time):
        self.class_time = time
    
    def getInstructor(self):
        return self.instructor_name
    def getLocation(self):
        return self.course_location
    def getTime(self):
        return self.class_time
    
    def printInfo(self):
        print(f"Course Number: {self.number}, Course Title: {self.title}, Instructor Name: {self.instructor_name}, Course Location: {self.course_location}, Class Time: {self.class_time}")

#Question 2
class Person:
    def __init__(self, name, birthDate, sex):
        self.mName = name
        self.mBirthDate = birthDate
        self.mSex = sex
    
    def setName(self, name):
        self.mName = name
    def setBirth(self, date):
        self.mBirthDate = date
    def setSex(self, sex):
        self.mSex = sex
    
    def getName(self):
        return self.mName
    def getBirthDate(self):
        return self.mBirthDate
    def getSex(self):
        return self.mSex
    
class Student(Person):
    def __init__(self, address, department, name, birthDate, sex):
        super().__init__(self, name, birthDate, sex)
        self.address = address
        self.department = department
    
    def setAddress(self, address):
        self.address = address
    def setDept(self, dept):
        self.department = dept
    
    def getAddress(self):
        return self.address
    def getDepartment(self):
        return self.department

class Teacher(Person):
    def __init__(self, rank, department, courseInfo, name, birthDate, sex):
        super().__init__(name, birthDate, sex)
        self.rank = rank
        self.department = department
        self.courseInfo = courseInfo
    
    def setRank(self, rank):
        self.rank = rank
    def setDept(self, dept):
        self.department = dept
    def setCourseInfo(self, info):
        self.courseInfo = info
    
    def getRank(self):
        return self.rank
    def getDepartment(self):
        return self.teachDept
    def getCourseInfo(self):
        return self.courseInfo

class GradTeachingFellow(Student, Teacher):
    def __init__(self, supervisor, name, birthDate, sex, address, department, rank, courseInfo, teachDept, teachName, teachDate, teachSex):
        Student.__init__(self, address, department, name, birthDate, sex)
        Teacher.__init__(self, rank, teachDept, courseInfo, teachName, teachDate, teachSex)
        self.supervisor = supervisor
    
    def setSupervisor(self, supervisor):
        self.supervisor = supervisor
    
    def getSupervisor(self):
        return self.supervisor
    
    def printInfo(self):
        print(f"Course Info: {Teacher.getCourseInfo()}, Supervisor: {self.getSupervisor()}, Student Department: {Student.getDepartment()}, Teacher Department: {Teacher.getDepartment()}.")
    
#Question 3
class Watch:
    def __init__(self):
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
    
    def setHour(self, hour):
        self.hour = hour
    def setMinutes(self, minutes):
        self.minutes = minutes
    def setSeconds(self, seconds):
        self.seconds = seconds
    
    def getHour(self):
        return self.hour
    def getMinutes(self):
        return self.minutes
    def getSeconds(self):
        return self.seconds
    
    def printTime(self):
        print(f"Current Time: {self.hour}:{self.minutes}:{self.seconds}")

class SmartWatch(Watch):
    def __init__(self, batteryPercentage):
        super().__init__()
        self.batteryPercentage = batteryPercentage
    
    def setBatteryPercentage(self, battery):
        self.batteryPercentage = battery
    def getBatteryPercentage(self):
        return self.batteryPercentage
    
    def printTime(self):
        print(f"Battery Percentage: {self.batteryPercentage}")
        print(f"Current Time: {self.hour}:{self.minutes}:{self.seconds}")
    def __add__(self, other):
        total_seconds = (self.hour + other.hour) * 3600 + (self.minutes + other.minutes) * 60 + (self.seconds + other.seconds)
        newHour = total_seconds // 3600
        total_seconds = total_seconds % 3600
        
        newMinutes = total_seconds // 60
        newSeconds = total_seconds % 60
        
        newWatch = SmartWatch(100)
        newWatch.setHour(newHour)
        newWatch.setMinutes(newMinutes)
        newWatch.setSeconds(newSeconds)
        
        return newWatch

def main():
    #Question 1
    #course1 = OfferedCourse(4930, "Intro to Python", "Mai Dahshan", "Building 15", "12:15 PM - 1:30 PM")
    #course1.printInfo()
    
    #Question 2
    #GTA = GradTeachingFellow("Krish", "Rahul", "01/31/02", "M", "27 King Street", "Math", "Professor", "Intro to Python", "Biology", "Emilia", "10/31/00", "F")
    #GTA.printInfo()
    
    #Question 3
    sWatch1 = SmartWatch(100)
    sWatch2 = SmartWatch(100)
    
    sWatch1.setHour(1)
    sWatch1.setMinutes(30)
    sWatch1.setSeconds(45)

    sWatch2.setHour(2)
    sWatch2.setMinutes(45)
    sWatch2.setSeconds(15)
    
    sWatch1.printTime()
    sWatch2.printTime()
    
    sWatch3 = sWatch1 + sWatch2
    sWatch3.printTime()

if __name__ == "__main__":
    main()