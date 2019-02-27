#!/usr/bin/python

import MySQLdb

# Open database connection
senha = input("Senha do Banco de Dados");

db = MySQLdb.connect("172.17.0.2","root",senha,"conhecimento" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT city.title FROM state INNER JOIN city ON city.id_state = state.id \
       WHERE letter = 'SC'"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      title = row[0]
      # Now print fetched result
      print "Cidade=%s" % \
             ( title )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
