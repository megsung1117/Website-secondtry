from flask import Flask, render_template, request, redirect, url_for,jsonify

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Taipei',
    'salary':'TWD 40000'
  },
  {
    'id':2,
    'title':'Python Engineer',
    'location':'Taipei',
    'salary':'TWD 50000'
  },
{
  'id':3,
  'title':'Front-end Engineer',
  'location':'Taipei',
  'salary':'TWD 50000'
}
]
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html',jobs=JOBS,company_name='Pyth')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080,debug=True)
  