# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:40:07 2024

@author: noodl
"""
import sqlite3
import tkinter as tk


class stdDatabase():
    def __init__(self):
        self.conn = sqlite3.connect("stdDatabase.db")
        self.cursor = self.conn.cursor()
    
    def createTable(self):
        #create student table
        try:
            self.cursor.execute("DROP TABLE IF EXISTS STUDENT")

            table = """CREATE TABLE IF NOT EXISTS STUDENT (
                STD_ID INT NOT NULL,
                STD_NAME CHAR(25) NOT NULL,
                STD_EMAIL VARCHAR(255),
                STD_GPA REAL NOT NULL,
                PRIMARY KEY(STD_ID)
            ); """

            self.cursor.execute(table)
        except Exception:
                print(Exception)
    
    def insertRecord(self, std_ID, std_Name, std_Email, std_GPA):
        
        try:
            sql = f''' INSERT INTO STUDENT
                        VALUES ({std_ID}, '{std_Name}', '{std_Email}', '{std_GPA}')'''
            self.cursor.execute(sql)
            return True
        except Exception:
            print(Exception)
            return False
    
    def updateRecord(self, std_ID, std_Name, std_Email, std_GPA):
        
        try:
            self.cursor.execute(f"UPDATE STUDENT SET STD_NAME = '{std_Name}', STD_EMAIL = '{std_Email}', STD_GPA = {std_GPA} WHERE STD_ID = {std_ID};")
            return True
        except Exception:
            print(Exception)
            return False
    
    def dataRecord(self):
        self.cursor.execute("SELECT * FROM STUDENT")
        return self.cursor.fetchall()
    
    def closeConnection(self):
        self.conn.close()

class StudentData(tk.Tk):
    def __init__(self):
        super().__init__()
        
        tk.Tk.__init__(self)
        
        self.ID = tk.IntVar()
        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.gpa = tk.DoubleVar()
        
        self.db = stdDatabase()
        
        self.geometry("400x300")
        self.title("Student Management System")
    
    def createStudentTable(self):
        self.db.createTable()
    
    def createLabel(self, rowNum, columnNum, labelText):
        label = tk.Label(self, text = labelText)
        label.grid(row=rowNum, column=columnNum)
    
    def createEntry(self, rowNum, columnNum, fieldName):
        entry = tk.Entry(self)
        entry.grid(row=rowNum, column=columnNum)
        
        if fieldName == 'ID':
            entry.config(textvariable=self.ID)
        elif fieldName == 'NAME':
            entry.config(textvariable=self.name)
        elif fieldName == 'EMAIL':
            entry.config(textvariable=self.email)
        elif fieldName == 'GPA':
            entry.config(textvariable=self.gpa)
    
    def createTextArea(self, rowNum, columnNum, text):
        textArea = tk.Text(self, height=5, width=30)
        textArea.grid(row=rowNum, column=columnNum)
        
        for line in text:
            textArea.insert(tk.END, line + '\n')
    
    def createButton(self, rowNum, columnNum, title, functionName):
        button = tk.Button(self, text=title, command=functionName)
        button.grid(row=rowNum, column=columnNum)
    
    def addStudent(self):
        addWindow = tk.Toplevel(self)
        addWindow.title("Add Student Record")
        addWindow.geometry("500x600")
        
        self.createLabel(0, 0, "Student ID")
        self.createEntry(0, 1, "ID")
        
        self.createLabel(1, 0, "Student Name")
        self.createEntry(1, 1, "NAME")
        
        self.createLabel(2, 0, "Student Email")
        self.createEntry(2, 1, "EMAIL")
        
        self.createLabel(3, 0, "Student GPA")
        self.createEntry(3, 1, "GPA")
        
        self.createButton(4, 0, "Add", self.addNewStudent)
        
    
    def addNewStudent(self):
        insert = self.db.insertRecord(self.ID.get(), self.name.get(), self.email.get(), self.gpa.get())
        
        if insert:
            tk.messagebox.showinfo("Success", "Student record added successfully.")
        else:
            tk.messagebox.showerror("Error", "Failed to add student record.")
    
    def updateStudent(self):
        self.updateWindow = tk.Toplevel(self)
        self.pdateWindow.title("Update Student Record")
        self.updateWindow.geometry("500x600")
        
        self.createLabel(0, 0, "Student ID")
        self.createEntry(0, 1, "ID")
        
        self.createLabel(1, 0, "Student Name")
        self.createEntry(1, 1, "NAME")
        
        self.createLabel(2, 0, "Student Email")
        self.createEntry(2, 1, "EMAIL")
        
        self.createLabel(3, 0, "Student GPA")
        self.createEntry(3, 1, "GPA")
        
        self.createButton(4, 0, "Update", self.updateExistingStudent)
    
    def updateExistingStudent(self):
        update = self.db.updateRecord(self.ID.get(), self.name.get(), self.email.get(), self.gpa.get())
        
        if update:
            tk.messagebox.showinfo("Success", "Student record updated successfully.")
        else:
            tk.messagebox.showerror("Error", "Failed to update student record.")
    
    def displayStudent(self):
        self.displayWindow = tk.Toplevel(self)
        self.displayWindow.title("Display Student Data")
        self.displayWindow.geometry("500x600")
        
        records = self.db.dataRecord()
        
        self.createLabel(0, 0, "Student Data")
        self.createTextArea(1, 1, records)

def main():
    std = StudentData()
    std.createStudentTable()
    
    std.createLabel(0, 0, "Student Management System")
    std.createButton(1, 0, "Add Student", "addStudent")
    
    std.createButton(2, 0, "Update Student", "updateStudent")
    std.createButton(3, 0, "Display Students", "displayStudent")
    
    std.mainloop()
    
    std.db.closeConnection()

if __name__ == "__main__":
    main()