from flask import Flask, jsonify, render_template,request
import database as db

JOBS = db.job_upload_from_db()

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('home.html',jobs=JOBS)


@app.route('/api/jobs/<id>')
def list_jobs(id):
  job = db.load_job(id)
  return jsonify(job)

@app.route('/job/<id>')
def show_job(id): 
   job = db.load_job(id)
   if job:
     return render_template('job.html', job=job)
   else:
     return "Job not found", 404

@app.route('/job/<id>/apply/', methods=['post','get'])
def apply_to_job(id):
  data = request.form
  job = db.load_job(id)
  db.add_application_to_db(id)
  return render_template('application_submitted.html',application=data, job=job)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080,debug=True)
  