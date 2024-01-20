from flask import Flask, jsonify, render_template
import database as db

JOBS = db.job_upload_from_db()

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('home.html',jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/job/<id>')
def show_job(id): 
   job = db.load_job(id)
   print(job)
   if job:
     return render_template('job.html', job=job)
     # return jsonify(job)
   else:
     return "Job not found", 404

  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080,debug=True)
  