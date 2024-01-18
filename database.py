import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# cursor.execute("UPDATE jobs SET requirements = 'The core concept of i-Buzz is a data-driven marketing strategy, developed through online corpus observation and mash-up data research to provide customers with in-depth data analysis results. In addition, through self-operated digital products, we want to mine user behavior data and provide a better product experience ' WHERE id=2")


# conn.commit()


# cursor.execute("UPDATE jobs SET requirements ='1. Analyze, design and implement systems and software, sometimes debugging.2. Skilled with Angular 10 or above.3. Familiar with Restful API integration is a must.4. Work with the engineers to solve frontend issues.' WHERE id = 4")

# conn.commit()
cursor.execute("SELECT * FROM jobs ")
rows = cursor.fetchall()
print(cursor)
conn.close()


def job_upload_from_db():
  conn = sqlite3.connect('mydatabase.db')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM jobs")
  
  rows = cursor.fetchall()
  
  job_list = []
  columns = [description[0] for description in cursor.description]
  for row in rows:
      job_dict = dict(zip(columns, row))
      job_list.append(job_dict)
  return job_list
