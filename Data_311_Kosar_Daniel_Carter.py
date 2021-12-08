#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DATA 311 - Mini Project
####Creation of the database in PostGRE SQL####

#Importing psycopg2
import psycopg2

# # *** The following code is used to create the database called "Company" ***
# conn = psycopg2.connect(database = 'postgres', user='postgres', password='Cd4225!', host="localhost", port='5432') #creating the connection
# conn.autocommit = True  #This is needed whenever a database is created

# cursor = conn.cursor() #creating a cursor for the connection

# create_db = '''CREATE database Company''' #creates a new database called "Company"

# cursor.execute(create_db) #executing the query that creates Company database
# print("Database Created ...")  #just to check if the code is running correctly

# conn.close() #closing the connection


#*** The following code is used to create the following tables: 1)Employee_Info, 2)Department_Info, 3)Project_Info
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE_INFO") #checks if a table with the same name already exists, if so, deletes it
cursor.execute("DROP TABLE IF EXISTS DEPARTMENT_INFO") #checks if a table with the same name already exists, if so, deletes it
cursor.execute("DROP TABLE IF EXISTS PROJECT_INFO") #checks if a table with the same name already exists, if so, deletes it

sql_table_1 = '''CREATE TABLE EMPLOYEE_INFO(
                 EMP_ID INT NOT NULL,
                 FIRST_NAME CHAR(20) NOT NULL,
                 LAST_NAME CHAR(20) NOT NULL,
                 GENDER CHAR(10) NOT NULL,
                 AGE INT,
                 JOB_TITLE CHAR(40) NOT NULL,
                 DEPT_ID INT NOT NULL,
                 SALARY INT NOT NULL,
                 CITY CHAR(30) NOT NULL
                 )'''

sql_table_2 = '''CREATE TABLE DEPARTMENT_INFO(
                 DEPT_ID INT NOT NULL,
                 DEPT_NAME CHAR(40) NOT NULL
                 )'''

sql_table_3 = '''CREATE TABLE PROJECT_INFO(
                 PROJ_ID INT NOT NULL,
                 PROJ_TYPE CHAR(40) NOT NULL,
                 DEPT_ID INT NOT NULL,
                 REVENUE INT,
                 COST INT,
                 DATE CHAR(20) NOT NULL,
                 CITY CHAR(30) NOT NULL
                 )'''

cursor.execute(sql_table_1)
cursor.execute(sql_table_2)
cursor.execute(sql_table_3)

print("Tables Created") #just checking that the code is running successfully

conn.commit()
conn.close()

#*** The following code is used to input the elements within the 3 tables ***
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')

cursor = conn.cursor()

statement = "INSERT INTO EMPLOYEE_INFO (EMP_ID,FIRST_NAME,LAST_NAME,GENDER,AGE,JOB_TITLE,DEPT_ID,SALARY,CITY) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
data = [(301,'Ellen','Patrick','Female',22,'Welder',401,63440,'Vancouver'),
        (302,'Alexander','Thompkins','Male',40,'Electrician',402,46697,'Calgary'),
        (303,'Zandra','Josephs','Female',24,'HVAC Technician',403,67818,'Edmonton'),
        (304,'Hayden','Dennis','Female',35,'Roofer',404,72028,'Vancouver'),
        (305,'Nydia','Benbow','Female',28,'Glazier',405,32145,'Vancouver'),
        (306,'James','Lyon','Male',34,'Machinist',406,84364,'Calgary'),
        (307,'Isiah','Wade','Other',28,'Landscaper',407,49480,'Calgary'),
        (308,'Natalia','Hermanson','Female',36,'Electrician',402,82645,'Edmonton'),
        (309,'Stirling','Crown','Male',20,'Machinist',406,61839,'Vancouver'),
        (310,'Brady','Washington','Other',40,'HVAC Technician',403,86682,'Calgary'),
        (311,'Pete','Whyte','Male',22,'Landscaper',407,83670,'Edmonton'),
        (312,'Berny','Kendrick','Other',40,'Welder',401,76908,'Edmonton'),
        (313,'Shevon','Jefferies','Male',29,'Electrician',402,43647,'Vancouver'),
        (314,'Dwain','Mark','Male',37,'Landscaper',407,47716,'Vancouver'),
        (315,'Dexter','Hampson','Other',27,'Roofer',404,41215,'Calgary')]

cursor.executemany(statement,data)

statement = "INSERT INTO DEPARTMENT_INFO (DEPT_ID,DEPT_NAME) VALUES(%s,%s)"
data = [(401,'Welding'),
        (402,'Electrical'),
        (403,'HVAC'),
        (404,'Roofing'),
        (405,'Glass'),
        (406,'Machinery'),
        (407,'Landscaping')]

cursor.executemany(statement,data)

statement = "INSERT INTO PROJECT_INFO (PROJ_ID,PROJ_TYPE,DEPT_ID,REVENUE,COST,DATE,CITY) VALUES(%s,%s,%s,%s,%s,%s,%s)"
data = [(5137,'Light Fixture',402,155387,69186,'2019/07/11','Calgary'),
        (5364,'Drilling',406,136323,53194,'2017/04/25','Calgary'),
        (5129,'Rock Removal',407,147134,116412,'2018/01/31','Calgary'),
        (5157,'Piping',403,127707,52584,'2015/05/14','Calgary'),
        (5220,'Framing',404,143374,131605,'2016/08/06','Calgary'),
        (5368,'Ductwork',403,146580,119152,'2016/11/02','Edmonton'),
        (5137,'Panel Hookup',402,159167,98854,'2019/05/16','Edmonton'),
        (5239,'Grass Maintenance',407,127062,70049,'2020/12/29','Edmonton'),
        (5374,'Hitch Weld',401,192914,102817,'2016/02/17','Edmonton'),
        (5075,'GMAW Weld',401,162643,136090,'2020/05/01','Vancouver'),
        (5026,'Shingling',404,130489,123545,'2017/10/23','Vancouver'),
        (5270,'Window Installation',405,131176,86811,'2020/03/18','Vancouver'),
        (5176,'Milling',406,195064,90195,'2017/12/31','Vancouver'),
        (5148,'Hot Tub Connection',402,114831,114248,'2016/08/03','Vancouver'),
        (5330,'Tree Planting',407,112476,116691,'2018/06/15','Vancouver')]

cursor.executemany(statement,data) #used to execute multiple queries at a single time

conn.commit()
conn.close()
###########################################################################################################################

####Query 1 (Aggregate Function)####

#Importing matplotlib
from matplotlib import pyplot as plt

#Form connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Connect Cursor
cursor = conn.cursor()

#Setting a years list
year_vector = [2015, 2016, 2017, 2018, 2019, 2020]

#Retrieving all counts of rows
retrieve_data ='''(SELECT COUNT(DATE) FROM PROJECT_INFO WHERE DATE LIKE '2015%')
UNION ALL
(SELECT COUNT(DATE) FROM PROJECT_INFO WHERE DATE LIKE '2016%')
UNION ALL
(SELECT COUNT(DATE) FROM PROJECT_INFO WHERE DATE LIKE '2017%')
UNION ALL
(SELECT COUNT(DATE) FROM PROJECT_INFO WHERE DATE LIKE '2018%')
UNION ALL
(SELECT COUNT(DATE) FROM PROJECT_INFO WHERE DATE LIKE '2019%')
UNION ALL
(SELECT COUNT(DATE) FROM PROJECT_INFO WHERE DATE LIKE '2020%')'''

#Cursor execute
cursor.execute(retrieve_data)
#Cursor fetchall
count_2015 = cursor.fetchall()

#Creating an empty list to store
all_counts = []

#Creating a for loop to make our values integers instead of tuples
for n in range(0,6):
    i = ''.join(map(str, count_2015[n]))
    all_counts += i

#Change our list of strings into a list of integers
integer_map = map(int, all_counts)
all_counts_final = list(integer_map)

#Printing query number and question
print("#Query 1#")
print("How many total projects does the company do in each year?")
#Plotting our values
plt.plot(year_vector, all_counts_final)
plt.xlabel('Year')
plt.ylabel('Number Of Projects')
plt.axis([2015, 2020, 0, 5])
plt.title("Total Projects Per Year", bbox = {'facecolor':'0.8', 'pad':2})
plt.show()

#Closing
conn.commit()
conn.close()

####Query 2 (Join Function) + (Aggregate Function)####

#Form a connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Cursor connection
cursor = conn.cursor()

#Retrieving total company revenue by department
retrieve_data ='''(SELECT DEPARTMENT_INFO.DEPT_NAME, SUM(PROJECT_INFO.REVENUE) FROM DEPARTMENT_INFO, PROJECT_INFO WHERE DEPARTMENT_INFO.DEPT_ID = PROJECT_INFO.DEPT_ID GROUP BY DEPARTMENT_INFO.DEPT_NAME)'''

#Cursor execute
cursor.execute(retrieve_data)
#Cursor fetchall
rev_by_dept = cursor.fetchall()

#Removing unwanted spaces using code from the following link
#https://www.geeksforgeeks.org/python-convert-list-of-tuples-into-list/
rev_by_dept = str(rev_by_dept).replace(' ', '')

#Turning the string back into a list
rev_by_dept = list(eval(rev_by_dept))

#Printing query number and question
print("#Query 2#")
print("What is the total company revenue attained each year?")
#Code to plot tuples
#This code: https://www.titanwolf.org/Network/q/744ee0e0-0596-40d7-be98-9096969a6e1a/y
#was used to construct our own
plt.bar(range(len(rev_by_dept)), [val[1] for val in rev_by_dept], color = ['green', 'gold', 'red', 'blue', 'brown', 'pink', 'orange'])
plt.xticks(range(len(rev_by_dept)), [val[0] for val in rev_by_dept])
plt.title("Total Company Revenue By Department", bbox = {'facecolor':'0.8', 'pad':2})
plt.xticks(rotation = 80)
plt.show()

#Closing
conn.commit()
conn.close()

####Query 3 (Aggregate Function)####

#Form connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Connect cursor
cursor = conn.cursor()

#Retrieving count of each gender in the company
sex_retrieval = '''(SELECT COUNT(GENDER) FROM EMPLOYEE_INFO GROUP BY GENDER)'''

#Cursor execute
cursor.execute(sex_retrieval)
#Cursor fetchall
count_of_sexes = cursor.fetchall()

#Changing list of tuples into a regular list using the code from this following link as structure
#https://www.geeksforgeeks.org/python-convert-list-of-tuples-into-list/
gender_count = [item for t in count_of_sexes for item in t]

#Retrieving the gender categories
gender_name = '''SELECT DISTINCT GENDER FROM EMPLOYEE_INFO'''

#Cursor execute
cursor.execute(gender_name)
#Cursor fetchall
gender_names = cursor.fetchall()

#Changing list of tuples into a regular list using the code from this following link as structure
gender_names_final = [item for t in gender_names for item in t]

#Printing query number and question
print("#Query 3#")
print("How many of the employees fall into each of the 3 different gender categories?")

#Pot the pie chart
plt.pie(gender_count, labels = gender_names_final, autopct='%.1f%%')
plt.title("Employee Gender Breakdown", bbox = {'facecolor':'0.8', 'pad':2})
plt.show()

#Closing
conn.commit()
conn.close()

####Query 4 (Aggregate Function)####

#Form connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Connect cursor
cursor = conn.cursor()

#Retrieving total company revenue by department
retrieved_employee_location ='''(SELECT COUNT(EMP_ID) FROM EMPLOYEE_INFO WHERE CITY LIKE 'Edmonton%')'''

#Cursor execute
cursor.execute(retrieved_employee_location)
#Cursor fetchall
edmonton_employees = cursor.fetchall()

#Changing list of tuples into a regular list
edmonton_employees = [item for t in edmonton_employees for item in t]

#Printing query number and question
print("#Query 4#")
print("How many employees work in Edmonton?")

#Print the output
result_4 = edmonton_employees[0] #***Fixed The Output For Query #4***
print("The number of employees that work in Edmonton is:", result_4, "\n")

#Closing
conn.commit()
conn.close()

####Query 5 (Aggregate Function)####

#Form connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Cursor connection
cursor = conn.cursor()

#Retrieving total company revenue by department
retrieved_employee_salary ='''(SELECT AVG(SALARY) FROM EMPLOYEE_INFO)'''

#Cursor execute
cursor.execute(retrieved_employee_salary)
#Cursor fetchall
average_salary = cursor.fetchall()

#Changing list of tuples into a regular list
average_salary = [item for t in average_salary for item in t]

#Changing from a decimal to an integer using the following stack overflow code
#https://stackoverflow.com/questions/10796690/converting-list-of-strings-with-decimal-places-to-ints-in-python
average_salary = [int(float(x)) for x in average_salary]

#Printing query number and question
print("#Query 5#")
print("What is the average employee salary?")

#Print the output
answer_5 = average_salary[0] #***Fixed The Output For Query #5***
print("The average employee salary is:", answer_5, "\n")

#Closing
conn.commit()
conn.close()

####Query 6 (Aggregate Function)####

#Form a connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Cursor connection
cursor = conn.cursor()

#Retrieving total company revenue by department
retrieved_salary_expense ='''(SELECT SUM(SALARY) FROM EMPLOYEE_INFO WHERE CITY LIKE 'Calgary%')'''

#Cursor execute
cursor.execute(retrieved_salary_expense)
#Cursor fetchall
salary_expense = cursor.fetchall()

#Changing list of tuples into a regular list
salary_expense = [item for t in salary_expense for item in t]

#Printing query number and question
print("#Query 6#")
print("What is the total salary expense for the employees in Calgary?")

#Print the output
answer_6 = salary_expense[0] #***Fixed The Output For Query #6***
print("The total salary expense for the Calgary employees is:", answer_6, "\n")

#Closing
conn.commit()
conn.close()

####Query 7 (Aggregate Function)####

#Form a connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Cursor connection
cursor_7 = conn.cursor()

#Retrieving average age of employees
question_7 = '''SELECT Avg(Age) FROM EMPLOYEE_INFO'''

#Cursor execute
cursor_7.execute(question_7)
#Cursor fetchall
result_7 = cursor_7.fetchall()

#extracting the answer (i.e. number) from the tuple
answer_7 = result_7[0][0]

#Formatting the answer to show 1 decimal
answer_7 = "{:.1f}".format(answer_7)

#Printing query number and question
print("#Query 7#")
print("What is the average age of all the employees?")

#Printing the output
print("The average age of all the employees is:", answer_7, "\n")

#closing
conn.commit()
conn.close()

####Query 8 (Join Function)####

#Form a connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Cursor connection
cursor = conn.cursor()

#Retrieving total company revenue by department
retrieved_employee_info ='''(SELECT EMPLOYEE_INFO.FIRST_NAME, EMPLOYEE_INFO.LAST_NAME, DEPARTMENT_INFO.DEPT_NAME FROM DEPARTMENT_INFO, EMPLOYEE_INFO WHERE DEPARTMENT_INFO.DEPT_ID = EMPLOYEE_INFO.DEPT_ID)'''

#Cursor execute
cursor.execute(retrieved_employee_info)
#Cursor fetchall
employee_department = cursor.fetchall()

#Printing query number and question
print("#Query 8#")
print("Display the first and last name of every employee, including the deparment they belong to:")

#Print employees names and departments & remove unwanted spaces
for rows in employee_department:
        print(str(rows).replace(' ', ''))
print("\n")

#Closing
conn.commit()
conn.close()

####Query 9 (Join Function)###

#Form a connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Connect cursor
cursor_9 = conn.cursor()

#Retrieve the number of employees aged greater than 30 that work in the Electrical department
question_9 = '''SELECT COUNT(EMPLOYEE_INFO.AGE)
                   from EMPLOYEE_INFO INNER JOIN DEPARTMENT_INFO
                   on EMPLOYEE_INFO.DEPT_ID = DEPARTMENT_INFO.DEPT_ID
                   WHERE (JOB_TITLE = 'Electrician') AND (AGE > 30)'''

#Cursor execute
cursor_9.execute(question_9)
#Cursor fetchall
result_9 = cursor_9.fetchall()

#extracting the answer (i.e. number) from the tuple
answer_9 = result_9[0][0] 

#Printing query number and question
print("#Query 9#")
print("How many employees aged greater than 30 work within the Electrical department?")

#Printing the output
print("The number of employees aged greater than 30 that work in the Electrical department is:", answer_9, "\n")

#Closing
conn.commit()
conn.close()

####Query 10 (Aggregate Function)####

#Form a connection
conn = psycopg2.connect(database='company',user='postgres',password='Cd4225!',host='localhost',port='5432')
#Connect cursor
cursor_10 = conn.cursor()

#Retrieving the age of the youngest employee
question_10 = '''SELECT Min(Age) FROM EMPLOYEE_INFO'''

#Cursor execute
cursor_10.execute(question_10)
#Cursor fetchall
result_10 = cursor_10.fetchall()

#extracting the answer (i.e. number) from the tuple
answer_10 = result_10[0][0] #extracting the answer (i.e. number) from the tuple

#Printing query number and question
print("#Query 10#")
print("What is the age of the youngest employee on staff?")

#Printing the output
print("The youngest employee on staff is of the following age:", answer_10)

#Closing
conn.commit()
conn.close()

