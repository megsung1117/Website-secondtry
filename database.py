import sqlite3

# conn = sqlite3.connect('mydatabase.db')
# cursor = conn.cursor()


# # cursor.execute("ALTER TABLE jobs ADD COLUMN status boolean")


# # cursor.execute("UPDATE jobs SET requirements ='1. Analyze, design and implement systems and software, sometimes debugging.\n2. Skilled with Angular 10 or above.\n3. Familiar with Restful API integration is a must.\n4. Work with the engineers to solve frontend issues.' WHERE id = 4")

# # conn.commit()
# cursor.execute("SELECT * FROM jobs ")
# rows = cursor.fetchall()
# print(rows)
# conn.close()


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

def load_job(id):
  conn = sqlite3.connect('mydatabase.db')

  cursor = conn.cursor()
  
  cursor.execute("SELECT * FROM jobs WHERE id = ?", (id,))
  
  row = cursor.fetchone()
  columns = [description[0] for description in cursor.description]
  if row:
    print(row)
    job_dict = dict(zip(columns, row))
    return job_dict
  else:
    return None

def add_job(job_dict):
  conn = sqlite3.connect('mydatabase.db')
  cursor = conn.cursor()
  cursor.execute("INSERT INTO jobs (title, responsibility, requirements, salary, location) VALUES (?,?,?,?,?)", (job_dict['title'], job_dict['responsibility'], job_dict['requirements'], job_dict['salary'], job_dict['location']))
   
  conn.commit()         
  conn.close()
  return cursor.lastrowid
  
def add_application_to_db(id):
  conn = sqlite3.connect('mydatabase.db')
  cursor = conn.cursor()
  cursor.execute("UPDATE jobs SET status = True WHERE id = ?", (id,))
  conn.commit()
  conn.close()
  return True