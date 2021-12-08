**SYSTEM REQUIREMENTS**

1) base installation of conda (in case of miniconda, a separate base installation of python is needed) 
Python version used in this program: 3.8.8

2) base installation of matplotlib library  
matplotlib version used in this program: 3.3.4 OR 3.4.3
command => pip install matplotlib 

3) installing PostgreSQL and pgAdmin4 database management system
link for download: https://www.postgresql.org/download/

4) base installation of psycopg2 PostgreSQL database adaptor 
psycopg2 version used in this program: 2.9.2 
command => pip3 install psycopg2-binary OR conda install -c conda-forge psycopg2  



**ABOUT THE PROGRAM**

This project represents a company providing welding, electrical, HVAC, roofing, glass work, machinery, and landscaping services. 

Our database consists of 3 tables: Employee Info (EMPLOYEE_INFO), Department Info (DEPARTMENT_INFO) and the Projects (PROJECT_INFO) accepted from clients. 

The Employee Info table keeps track of employee ID (EMP_ID), with their first and last names, gender (male, female, other), age, job title along with the specific department ID (DEPT_ID), their salary and the city they are located in. 

The Department Info table includes the names of different departments (DEPT_NAME) and the ID number (DEPT_ID) they are represented by in other tables. 

The projects table consists of the type of project represented by different project IDs refering to a project type, the department ID responsible for project completion, the date and city where the project was accepted in addition to the cost and the revenue per project. 

There are 10 queries written to explore the relationships between different entities in these tables. 

For the first query, we have used matplotlib libraries to show the total number of projects per year using a line chart. To achieve this, we have used the UNION ALL function to compile the number of projects after filtering the years from the PROJECT_INFO table. 

For the second query, we used the SUM aggregate function and joined the DEPARTMENT_INFO and PROJECT_INFO tables to display the total revenue of the company per department in a bar graph. Similar to the previous query, we used matplotlib library for the visualization. To join the two tables, we used DEPT_ID as foreign key to connect the name of the departments to the inputted revenue. 

The output of query 3 is represented in a pie chart using matplotlib library. We used the COUNT aggregate function from the EMPLOYEE_INFO table to compile the number of the 3 gender categories in the company. The green portion represents the proportion of 'male' in the company while orange represents the 'female' and blue is for 'other'.  

Query 4 aims to output the number of company employees that are located in Edmonton. To achieve this, we used the COUNT aggregate function from the EMPLOYEE_INFO table to count the number of occurances of Edmonton in the City attribute. 

Query 5 uses the AVG aggregate function to output the average employee salary in the company. We selected the salary entity from the Employee Info table to get the desired result.  

Query 6 uses the SUM aggregate function to output the total salary expense in Calgary. We compiled all employee salaries where the corresponding input of the City entity was Calgary. 

Query 7 aims to output the average age of all the employees in the company. In order to achieve this, we use an AVE aggregate function in the Employee Info table to take the average of all enteries from the Age column. 

The purpose of query 8 is to display the full name of all employees along with the departments of their occupation. To achieve this, DEPARTMENT_INFO and EMPLOYEE_INFO tables were joined using DEPT_ID as foreign key. 

The purpose of query 9 is to see how many employees are in the electrical department above the age of 30. This query was executed through the JOIN function between DEPARTMENT_INFO and EMPLOYEE_INFO using DEPT_ID as the foreign key. The JOB_TITLE was filtered as 'Electrician' from EMPLOYEE_INFO (connecting to DEPT_ID of 402) and AGE > 30. 

For the last query, we wanted to select the age of the youngest employee within the company. For this purpose, we used the MIN aggregate function to output the minimum age from EMPLOYEE_INFO.
