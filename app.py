from flask import Flask, jsonify, render_template
import database as db

  
JOBS = db.job_upload_from_db()

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('home.html',jobs=JOBS,company_name='Pyth')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080,debug=True)
  