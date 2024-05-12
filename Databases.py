# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:50:18 2024

def createCustomerEntry(customer_id, fName, lName, email):
    executes an sql insert statement for the customers table with values passed through parameters

def createOrderEntry(order_id, customer_id, total):
    executes an sql insert statement for the orders table with values passed through parameters

@author: noodl
"""

import sqlite3

#Create a database named SQL_Lab
conn = sqlite3.connect("SQL_Lab.db")
cursor = conn.cursor()

#create table
cursor.execute("DROP TABLE IF EXISTS Customers")

table = """CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT NOT NULL,
    customer_firstName CHAR(25) NOT NULL,
    customer_lastName CHAR(25) NOT NULL,
    customerEmail VARCHAR(255),
    PRIMARY KEY(customer_id)
); """

cursor.execute(table)

cursor.execute("DROP TABLE IF EXISTS Orders")

table = """CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    total INTEGER NOT NULL,
    PRIMARY KEY(order_id),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
); """

cursor.execute(table)

def createCustomerEntry(customer_id, fName, lName, email):
    sql = f''' INSERT INTO Customers
                VALUES ({customer_id}, '{fName}', '{lName}', '{email}')'''
    cursor.execute(sql)

def createOrderEntry(order_id, customer_id, total):
    sql = f''' INSERT INTO Orders
                VALUES ({order_id}, {customer_id}, {total})'''
    cursor.execute(sql)

#Entry Customer
createCustomerEntry(100, 'John', 'Svendson', 'jsvendson@gmail.com')
createCustomerEntry(200, 'Stephen', 'Adams', 'sadams@gmail.com')
createCustomerEntry(300, 'Kari', 'Pettersen', 'kpettersen@gmail.com')
createCustomerEntry(400, 'James', 'McClure', 'jmcClure@gmail.com')

#Entry Orders
createOrderEntry(1000, 100, 100)
createOrderEntry(1001, 400, 20)
createOrderEntry(1002, 100, 40)
createOrderEntry(1003, 200, 500)
createOrderEntry(1004, 200, 60)
createOrderEntry(1005, 300, 900)

#Queries
cursor.execute('SELECT COUNT(*) AS total_orders FROM Orders WHERE total > 100;')
print(cursor.fetchall())

cursor.execute('SELECT c.customer_lastName, o.order_id, o.total FROM Customers c INNER JOIN Orders o ON c.customer_id = o.customer_id;')
print(cursor.fetchall())

#Updates
cursor.execute("UPDATE Orders set total=1000 where order_id = 1005;")

cursor.execute("DELETE FROM Customers WHERE customer_lastName = 'McClure';")

cursor.execute("ALTER TABLE Orders RENAME COLUMN total TO orderTotal;")

conn.close()