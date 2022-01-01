from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def index():
  dt_now = datetime.datetime.now()
  values = { "name": "test" , "date" : dt_now}
  return render_template('index.html', data=values)

# Second Page
@app.route("/test")
def test():
  values = { "message":"Hello! This is test page." }
  return render_template('test.html', data=values)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
