# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:14:48 2024

@author: noodl
"""

import tkinter as tk

class RegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Registration Form")
        
        # StringVar objects
        self.name_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.contact_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.country_var = tk.StringVar()
        self.checkbox_var = tk.StringVar()
        
        self.createLabel(0, 0, "Name:")
        self.createNameEntry(0, 1)
        
        self.createLabel(1, 0, "Password:")
        self.createPasswordEntry(1, 1)
        
        self.createLabel(2, 0, "Contact:")
        self.createContactEntry(2, 1)
        
        self.createLabel(3, 0, "Email:")
        self.createEmailEntry(3, 1)
        
        self.createLabel(4, 0, "Country:")
        self.dropDownList(4, 1, ['USA', 'Canada', 'UK'])
        
        self.createLabel(5, 0, "Age:")
        self.spinBox(5, 1, 18, 100)
        
        self.createLabel(6, 0, "Gender:")
        self.radioButton(6, 1, "Male", "male")
        self.radioButton(6, 2, "Female", "female")
        
        self.checkButton(7, 0, "Subscribe", "No", "Yes")
        
        self.createButton(8, 1, "Submit", self.submit_form)
        
    def createLabel(self, rowNum, columnNum, labelText):
        label = tk.Label(self, text=labelText)
        label.grid(row=rowNum, column=columnNum, padx=5, pady=5, sticky='w')
        
    def createNameEntry(self, rowNum, columnNum):
        entry = tk.Entry(self, textvariable=self.name_var)
        entry.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def createPasswordEntry(self, rowNum, columnNum):
        entry = tk.Entry(self, textvariable=self.password_var, show='*')
        entry.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def createContactEntry(self, rowNum, columnNum):
        entry = tk.Entry(self, textvariable=self.contact_var)
        entry.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def createEmailEntry(self, rowNum, columnNum):
        entry = tk.Entry(self, textvariable=self.email_var)
        entry.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def spinBox(self, rowNum, columnNum, fromRange, toRange):
        spinbox = tk.Spinbox(self, from_=fromRange, to=toRange)
        spinbox.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def radioButton(self, rowNum, columnNum, radioText, radioValue):
        radio = tk.Radiobutton(self, text=radioText, variable=self.checkbox_var, value=radioValue)
        radio.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def dropDownList(self, rowNum, columnNum, listOfCountries):
        dropdown = tk.OptionMenu(self, self.country_var, *listOfCountries)
        dropdown.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def checkButton(self, rowNum, columnNum, checkText, checkOffValue, checkOnValue):
        checkbox = tk.Checkbutton(self, text=checkText, variable=self.checkbox_var, onvalue=checkOnValue, offvalue=checkOffValue)
        checkbox.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def createButton(self, rowNum, columnNum, buttonText, command):
        button = tk.Button(self, text=buttonText, command=command)
        button.grid(row=rowNum, column=columnNum, padx=5, pady=5)
        
    def submit_form(self):
        print("Submitting form...")
        # Implement form submission logic here

# Example usage
if __name__ == "__main__":
    app = RegistrationForm()
    app.mainloop()