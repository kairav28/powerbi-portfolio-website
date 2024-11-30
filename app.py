from flask import Flask, render_template, jsonify

app = Flask(__name__)

DASHBOARDS = [
  {
    'id': 1,
    'title': 'Verification',
    'link': 'https://www.db1.com',
    'about': 'This dashboard showcases data from different verification exercises which were done to understand if teachers were assessing students appropriately and entering approprite results'
  },
  {
    'id': 2,
    'title': 'Gender-wise',
    'link': 'https://www.db2.com',
    'about': 'This dashboard analyses data of students with an emphasis on outcomes based on gender'
  },
  {
    'id': 3,
    'title': 'Mentoring',
    'link': 'https://www.db3.com',
    'about': 'This dashboard analyses data recorded by mentors following their visits to class rooms'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', dashboards=DASHBOARDS)

@app.route("/api/dashboards")
def list_dashboards():
  return jsonify(DASHBOARDS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
