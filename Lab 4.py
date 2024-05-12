# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:24:37 2024

@author: noodl
"""

import sqlite3
import tkinter as tk

class stdDatabase:
    def __init__(self, db_name):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database:", e)

    def createTable(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT (
                                STD_ID INTEGER PRIMARY KEY,
                                STD_NAME TEXT,
                                STD_EMAIL TEXT,
                                STD_GPA REAL)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error creating table:", e)

    def insertRecord(self, std_id, std_name, std_email, std_gpa):
        try:
            self.cursor.execute('''INSERT INTO STUDENT (STD_ID, STD_NAME, STD_EMAIL, STD_GPA)
                                VALUES (?, ?, ?, ?)''', (std_id, std_name, std_email, std_gpa))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error inserting record:", e)
            return False

    def updateRecord(self, std_id, std_name, std_email, std_gpa):
        try:
            self.cursor.execute('''UPDATE STUDENT SET STD_NAME=?, STD_EMAIL=?, STD_GPA=?
                                WHERE STD_ID=?''', (std_name, std_email, std_gpa, std_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Error updating record:", e)
            return False

    def dataRecord(self):
        try:
            self.cursor.execute('''SELECT * FROM STUDENT''')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("Error fetching records:", e)
            return []

    def closeConnection(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print("Error closing connection:", e)


class StudentData(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ID = tk.IntVar()
        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.gpa = tk.DoubleVar()
        self.db = stdDatabase("student.db")
        self.geometry("400x300")
        self.title("Student Management System")

    def createStudentTable(self):
        self.db.createTable()

    def createLabel(self, rowNum, columnNum, labelText):
        label = tk.Label(self, text=labelText)
        label.grid(row=rowNum, column=columnNum)

    def createEntry(self, rowNum, columnNum, fieldName):
        entry = tk.Entry(self)
        if fieldName == 'ID':
            entry["textvariable"] = self.ID
        elif fieldName == 'Name':
            entry["textvariable"] = self.name
        elif fieldName == 'EMAIL':
            entry["textvariable"] = self.email
        elif fieldName == 'GPA':
            entry["textvariable"] = self.gpa
        entry.grid(row=rowNum, column=columnNum)

    def createTextArea(self, rowNum, columnNum, text):
        text_area = tk.Text(self, height=10, width=30)
        text_area.grid(row=rowNum, column=columnNum)
        for item in text:
            text_area.insert(tk.END, item + "\n")

    def createButton(self, rowNum, columnNum, button_title, functionName):
        button = tk.Button(self, text=button_title, command=eval("self." + functionName))
        button.grid(row=rowNum, column=columnNum)

    def addStudent(self):
        add_window = tk.Toplevel(self)
        add_window.title("Add Student Record")
        add_window.geometry("200x200")
        
        idLabel = tk.Label(add_window, text='ID')
        idLabel.grid(row=0, column=0)
        idEntry = tk.Entry(add_window, textvariable=self.ID)
        idEntry.grid(row=0, column=1)
        
        nameLabel = tk.Label(add_window, text='Name')
        nameLabel.grid(row=1, column=0)
        nameEntry = tk.Entry(add_window, textvariable=self.name)
        nameEntry.grid(row=1, column=1)
        
        emailLabel = tk.Label(add_window, text='Email')
        emailLabel.grid(row=2, column=0)
        emailEntry = tk.Entry(add_window, textvariable=self.email)
        emailEntry.grid(row=2, column=1)
        
        gpaLabel = tk.Label(add_window, text='GPA')
        gpaLabel.grid(row=3, column=0)
        gpaEntry = tk.Entry(add_window, textvariable=self.gpa)
        gpaEntry.grid(row=3, column=1)
        
        addNewButton = tk.Button(add_window, text="Add", command=self.addNewStudent)
        addNewButton.grid(row=4, column=0)

    def addNewStudent(self):
        std_id = self.ID.get()
        std_name = self.name.get()
        std_email = self.email.get()
        std_gpa = self.gpa.get()
        if self.db.insertRecord(std_id, std_name, std_email, std_gpa):
            print("Record added successfully")
        else:
            print("Failed to add record")

    def updateStudent(self):
        update_window = tk.Toplevel(self)
        update_window.title("Update Student Record")
        update_window.geometry("200x200")
        
        idLabel = tk.Label(update_window, text='ID')
        idLabel.grid(row=0, column=0)
        idEntry = tk.Entry(update_window, textvariable=self.ID)
        idEntry.grid(row=0, column=1)
        
        nameLabel = tk.Label(update_window, text='Name')
        nameLabel.grid(row=1, column=0)
        nameEntry = tk.Entry(update_window, textvariable=self.name)
        nameEntry.grid(row=1, column=1)
        
        emailLabel = tk.Label(update_window, text='Email')
        emailLabel.grid(row=2, column=0)
        emailEntry = tk.Entry(update_window, textvariable=self.email)
        emailEntry.grid(row=2, column=1)
        
        gpaLabel = tk.Label(update_window, text='GPA')
        gpaLabel.grid(row=3, column=0)
        gpaEntry = tk.Entry(update_window, textvariable=self.gpa)
        gpaEntry.grid(row=3, column=1)
        
        addNewButton = tk.Button(update_window, text="Update", command=self.updateExistingStudent())
        addNewButton.grid(row=4, column=0)


    def updateExistingStudent(self):
        std_id = self.ID.get()
        std_name = self.name.get()
        std_email = self.email.get()
        std_gpa = self.gpa.get()
        if self.db.updateRecord(std_id, std_name, std_email, std_gpa):
            print("Record updated successfully")
        else:
            print("Failed to update record")

    def displayStudent(self):
        display_window = tk.Toplevel(self)
        display_window.title("Display Student Data")
        data = self.db.dataRecord()
        
        stdText = tk.Text(display_window, height=10, width=30)
        stdText.grid(row=0, column=0)
        for item in data:
            stdText.insert(tk.END, item + "\n")


def main():
    std = StudentData()
    std.createStudentTable()
    std.createLabel(0, 0, "Student Management System")
    std.createButton(1, 0, "Add Student", "addStudent")
    std.createButton(2, 0, "Update Student", "updateStudent")
    std.createButton(3, 0, "Display Students", "displayStudent")
    std.mainloop()

if __name__ == "__main__":
    main()
