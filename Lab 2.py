# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:29:44 2024

Q1) Create a "Dog" class. Dog class has 

-three attributes: name (String), breed (String), and age (int)
-a constructor that accepts three arguments to set name, breed, and age attributes
-Create setter and getter functions to get and set values for all attributes (i.e.,  setName,getName, setBreed, getBreed, setAge, and getAge) 
-Override __str__() python method that prints the following dog’s name, breed, and age
-Create a main method and within the main method instantiate an instances(object) of the Dog class, denoting it as dog1 
-print the values of attributes using getters
-use setters to update the values of attributes 
-print  dog1 object

Q2) Create a "FoodItem" class. FoodItem class has 

-four attributes: name (String), fat (double),  carbs (double),  and protein (double)
-a constructor that accepts no arguments. Inside the constructor, set the values of attributes from user input
-Create setter and getter functions to get and set values for all attributes
-Override __str__() python method that prints nutritional information using values for all attributes
-Create a method getCalories that calculates the calories per serving. getCalories takes as input the numServings (double) and returns calculated calories
-calCalories = ((fat * 9) + (carbs * 4) + (protein * 4)) * numServings

 
-Create a main method and within the main method instantiate two instances(object) of the FoodItem class, denoting it as foodItem1, and foodItem2 
-print the values of attributes using getters
-use setters to update the values of attributes 
-print  foodItem1 and foodItem2 objects
-Call getCalories method for the two objects (foodItem1 and foodItem2) with different values for numServings
 

Q3) Create a "Course" class. Course class has 

-four attributes: name (String), major  (String),  creditHours (int),  and studentNames (List of Names)
-a constructor that accepts three arguments: name, major, and  creditHours. Inside the constructor, set studentNames to empty list
-Create setter and getter functions to get and set values for name, major, and  creditHours. 
-Create a method AddStudent that adds a student to studentNames list  AddStudent takes as input a student name and doesn’t return anything
-Create a method findStudent that lookup a student in  studentNames list .  findStudent takes as input a student name and returns true if student exists, otherwise returns false
-Override __str__() python method that prints about course name, major,  creditHours, number of students in the class and their name

-Create a main method and within the main method instantiate two instances(object) of the Course class, denoting it as course1, and course2 
-print the values of attributes using getters
-use setters to update the values of attributes 
-Add three students to course1 and five students to  course2 
-print  course1 and course2 objects
-Call findStudent twice with course1 and course2 objects. On the first call, use a name that exists in the studentNames, and on the second call, use a name that doesn’t exist in the studentNames.

Q4) Create a "Triangle" class. Triangle class has 

-two attributes: base (double) and height (double)
-a constructor that accepts two arguments to base and height
-Create setter and getter functions to get and set values for all attributes
-Override __str__() python method that prints information about triangle 
-Create an area method. It takes no input and returns the area of triangle using the formula below
    -A = (height * base) / 2
    
-Create a main method and within the main method instantiate a list of ten instances(object) of the Triangle class, denoting it as triangles. Use a loop to read the base and height for each object from the user input 
-print the values of attributes using getters (use loops)
-print  all the objects in the list (triangles) (use loops)
-Call the area method for all objects in the list (triangles) (use loops)

Q5) Create a "WellsFargoBankInfo" class. WellsFargoBankInfo class has 

-two attributes: branches (dictionary), employees   (list of dictionaries)
-a constructor that accepts no arguments and sets branches to an empty dictionary and employees to an empty list
-Create a method Addbank that adds a new record to branches with branch name and id. (ex: {'JAXHodes':100}
-Create a method AddEmp that adds a new record in the employees list. (ex: [{'Name':"James Adams",'Title':'Manager','Salay':4000000,'Age':40, 'ID'}]
-Create a method findbank that searches the branches by name
-Create a method findEmp that searches the employees by name
-Create a method removebank that removes a branch from the branches by name
-Create a method removeEmp that removes an employee from  employees by ID
-Override __str__() python method that prints information about branches and employees


@author: Rahul Thadhani
"""

#Question 1
class Dog:
    def __init__(self, name, breed, age):
        self.__name = name
        self.__breed = breed
        self.__age = age
        
    def setName(self, name):
        self.__name = name
    def setBreed(self, breed):
        self.__breed = breed
    def setAge(self, age):
        self.__age = age
    
    def getName(self):
        return self.__name
    def getBreed(self):
        return self.__breed
    def getAge(self):
        return self.__age
    
    def __str__(self):
        return f"Name: {self.__name}, Breed: {self.__breed}, Age: {self.__age}"

#Question 2
class FoodItem:
    def __init__(self):
        self.__name = input("Enter Food Name: ")
        self.__fat = float(input("Enter Fat Content (g): "))
        self.__carbs = float(input("Enter Carb Content (g): "))
        self.__protein = float(input("Enter Protein Content (g): "))
        
    def setName(self, name):
        self.__name = name
    def setFat(self, fat):
        self.__fat = fat
    def setCarb(self, carbs):
        self.__carbs = carbs
    def setProtein(self, protein):
        self.__protein = protein
    
    def getName(self):
        return self.__name
    def getFat(self):
        return self.__fat
    def getCarb(self):
        return self.__carbs
    def getProtein(self):
        return self.__protein
    
    def __str__(self):
        return f"Name: {self.__name}, Fat: {self.__fat}g, Carbs: {self.__carbs}g, Protein: {self.__protein}g"
    
    def getCalories(self, numServings):
        return ((self.__fat * 9) + (self.__carbs * 4) + (self.__protein * 4)) * numServings
    
#Question 3
class Course:
    def __init__(self, name, major, creditHours):
        self.__name = name
        self.__major = major
        self.__creditHours = creditHours
        self.__studentNames = []
        
    def setName(self, name):
        self.__name = name
    def setMajor(self, major):
        self.__major = major
    def setCreditHours(self, creditHours):
        self.__creditHours = creditHours
    
    def getName(self):
        return self.__name
    def getMajor(self):
        return self.__major
    def getCredit(self):
        return self.__creditHours
    
    def AddStudent(self, name):
        self.__studentNames.append(name)
    
    def findStudent(self, name):
        return name in self.__studentNames
    
    def __str__(self):
        num = len(self.__studentNames)
        stuNames = ", ".join(self.__studentNames)
        return f"Course Name: {self.__name}, Major: {self.__major}, Credit Hours: {self.__creditHours}, Total Students: {num}, Student Names: {stuNames}"
    
#Question 4
class Triangle:
   def __init__(self, base, height):
      self.__base = base
      self.__height = height
     
   def setBase(self, base):
      self.__base = base
   def setHeight(self, height):
      self.__height = height
   
   def getBase(self):
      return self.__base
   def getHeight(self):
      return self.__height
   
   def __str__(self):
      return f"Base: {self.__base}, Height: {self.__height}"
   
   def area(self):
      return (self.__height * self.__base) / 2

#Question 5
class WellsFargoBankInfo:
   def __init__(self):
      self.__branches = {}
      self.__employees = []
   
   def addBank(self, name, id):
      self.__branches[name] = id
   def addEmp(self, name, title, salary, age, id):
      self.__employees.append({"Name": name, "Title": title, "Salary": salary, "Age": age, "ID": id})
   def findBank(self, name):
      return name in self.__branches
   def findEmp(self, name):
       for x in self.__employees:
           if x['name'] == name:
               return True
       return False
   def removeBank(self, name):
      del self.__branches[name]
   def removeEmp(self, id):
      for i, employee in enumerate(self.employees):
            if employee['ID'] == id:
                del self.__employees[i]
   def __str__(self):
      print(self.__branches, "\n")
      for x in self.__employees:
         print(x, "\n")

def main():
    #Question 1
    dog1 = Dog("Comet", "Chihuahua", 7)
    
    print("Name:", dog1.getName(), "Breed:", dog1.getBreed(), "Age:", dog1.getAge())
    
    dog1.setName("Journey")
    dog1.setBreed("German Shepherd")
    dog1.setAge(1)
    
    print(dog1, "\n")
    
    #Question 2
    foodItem1 = FoodItem()
    print("\n")
    foodItem2 = FoodItem()
    print("\n")
    
    print("Name:", foodItem1.getName(), "Fat:", foodItem1.getFat(), "Carbs:", foodItem1.getCarb(), "Protein:", foodItem1.getProtein(), "\n")
    print("Name:", foodItem2.getName(), "Fat:", foodItem2.getFat(), "Carbs:", foodItem2.getCarb(), "Protein:", foodItem2.getProtein(), "\n")
    
    foodItem1.setName("Salad")
    foodItem1.setFat(5.0)
    foodItem1.setCarb(20.0)
    foodItem1.setProtein(10.0)
    
    foodItem2.setName("Burger")
    foodItem2.setFat(10.0)
    foodItem2.setCarb(15.0)
    foodItem2.setProtein(10.0)
    
    print(foodItem1)
    print(foodItem2)
    
    print("Calories:", foodItem1.getCalories(3))
    print("Calories:", foodItem2.getCalories(2))
    
    #Question 3
    course1 = Course("Python", "Computer Science", 3)
    course2 = Course("Data Structure", "Computer Science", 3)
    
    print("Course Name:", course1.getName(), "Major:", course1.getMajor(), "Credit Hours:", course1.getCredit(), "\n")
    print("Course Name:", course2.getName(), "Major:", course2.getMajor(), "Credit Hours:", course2.getCredit(), "\n")
    
    course1.AddStudent("Rahul")
    course1.AddStudent("Thomas")
    course1.AddStudent("Alex")
    
    course2.AddStudent("Mutasim")
    course2.AddStudent("Sayf")
    course2.AddStudent("Anthony")
    course2.AddStudent("D'Angelo")
    course2.AddStudent("Lebron")
    
    print(course1, "\n", course2, "\n")
    print(course1.findStudent("Rahul"))
    print(course2.findStudent("Tyrone"))
    
    #Question 4
    triangles = []
    i = 0
    j = 1
    k = 1
    while i < 10:
        triangles.append(Triangle(int(input(f"Enter the base of the triangle {i + 1}: ")), int(input(f"Enter the height of the triangle {i + 1}: "))))
        i = i + 1
    for x in triangles:
        print(f"Base {k}:, {x.getBase()}, Height {k}:, {x.getHeight()}")
        k = k + 1
    for x in triangles:
        print(x, "\n")
    for x in triangles:
        print(f"Area Triangle {j}: {x.area()}")
        j = j + 1
       
    
if __name__ == "__main__":
    main()
    