##import sqlite3
##conn= sqlite3.connect('test.db')
##conn.execute(''' create table loan (
##loantype text,
##rate int
##)''')
##
##conn.execute("insert into loan values ('House Loan',9)")
##conn.execute("insert into loan values ('Education',11)")
##conn.execute("insert into loan values ('Modgage',10)")
##conn.execute("insert into loan values ('Gold',11)")
##conn.execute("insert into loan values ('Personal',13)")

##sql_command = "SELECT * FROM loan WHERE loantype = "+id
##
##            cur = conn.cursor()
##            cur.execute(sql_command)
##            result = cur.fetchall()

def houseloan(p,n):
    r=9
    r = r / (12 * 100); 
    n = n * 12;
    emi = (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1); 
   
    return emi

def education(p,n):
    r=11
    r = r / (12 * 100); 
    n = n * 12;
    emi = (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1); 
   
    return emi

def modgage(p,n):
    r=10
    r = r / (12 * 100); 
    n = n * 12;
    emi = (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1); 
   
    return emi

def gold(p,n):
    r=11
    r = r / (12 * 100); 
    n = n * 12;
    emi = (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1); 
   
    return emi

def personal(p,n):
    r=13
    r = r / (12 * 100); 
    n = n * 12;
    emi = (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1); 
   
    return emi

cases={
        1:houseloan,
        2:education,
        3:modgage,
        4:gold,
        5:personal
        }
    
    
print("============== EMI Calculator for Banking Operation========")
print(" The table below shows Loan type and their InterestRate")
print("1. House Loan    9%")
print("2. Education     11%")
print("3. Modgage       10%")
print("4. Gold          11%")
print("5. Personal      13%")

print("Enter Principal amount and Period")
print("For Different Types of Loan type choose the option given above")


principal=int(input('enter principal amount'))
period=int(input('Enter Loan Period in Years'))
choice=int(input("Make a choice"))

print(cases[choice](principal,period))








