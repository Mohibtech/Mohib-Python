import cx_Oracle

# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("hr", "hr", "localhost/far.genie.com")
cursor = connection.cursor()

statement="""
          SELECT first_name, last_name FROM hr.employees 
          where employee_id > :eid 
          and department_id=:did
          """

cursor.execute(statement, (100,10))
#cursor.execute(statement, {'eid':100, 'did':10}) # Another to bind variables with names

result = cursor.fetchall()
for row in result:
    print(row[0],row[1])
